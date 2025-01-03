import numpy as np
import importlib
from utils import OutToFile, round_to_significant_figures
import time
import matplotlib.pyplot as plt
import os

class Solver:
    def __init__(self, Nx, Ny, task_num):
        self.M = importlib.import_module('task' + str(task_num))
        self.Nx = Nx
        self.Ny = Ny
        self.h_x = self.M.X / (self.Nx - 1)
        self.h_y = self.M.Y / (self.Ny - 1)

        self.p = np.zeros((self.Nx, self.Ny))


    def init(self, v):
        for i in range(self.Nx):
            v[i, 0] = self.get_grid_func(self.M.g_down, i, 0)
            v[i, -1] = self.get_grid_func(self.M.g_up, i, 0)

        for j in range(self.Ny):
            v[0, j] = self.get_grid_func(self.M.g_l, 0, j)
            v[-1, j] = self.get_grid_func(self.M.g_r, 0, j)

        tmp = (v[0][0] + v[0][-1] + v[-1][0] + v[-1][-1]) / 4
        for i in range(1, self.Nx - 1):
            for j in range(1, self.Ny - 1):
                v[i][j] = tmp

    def get_grid_func(self, func, i, j):
        return func(i * self.h_x, j * self.h_y)

    def get_grid_k1(self, i, j):
        return self.M.k1(i * self.h_x, j * self.h_y, self.p[i, j])

    def get_grid_k2(self, i, j):
        return self.M.k2(i * self.h_x, j * self.h_y, self.p[i, j])

    def out(self):
        o = OutToFile('out_'+ str(TaskNumber))
        o.write_numpy_to_csv(self.p)

    def Dx(self, i, j, p):
        v1_ = self.get_grid_func(self.M.v1, i, j)
        if v1_ > 0:
            return  v1_ * (p[i, j] - p[i - 1, j]) / self.h_x
        return v1_ * (p[i + 1, j] - p[i, j]) / self.h_x

    def Dy(self, i, j, p):
        v2_ = self.get_grid_func(self.M.v2, i, j)
        if v2_ > 0:
            return v2_ * (p[i, j] - p[i, j - 1]) / self.h_y
        return v2_ *  (p[i, j + 1] - p[i, j]) / self.h_y

    def ax(self, i, j):
        return (self.get_grid_k1(i, j) + self.get_grid_k1(i - 1, j)) / 2.

    def ay(self, i, j):
        return (self.get_grid_k2(i, j) + self.get_grid_k2(i, j - 1)) / 2.

    def Lx(self, i, j, p):
        return (self.ax(i + 1, j) * (p[i + 1, j] - p[i, j]) - self.ax(i, j) * (p[i, j] - p[i - 1, j])) / np.power(self.h_x, 2)

    def Ly(self, i, j, p):
        return (self.ay(i, j + 1) * (p[i, j + 1] - p[i, j]) - self.ay(i, j) * (p[i, j] - p[i, j - 1])) / np.power(self.h_y, 2)

    def A(self, i, j, p):
        # print(-(self.Lx(i, j, p) + self.Ly(i, j, p)) + self.Dx(i, j, p) + self.Dy(i, j, p) - self.get_grid_func(self.M.f, i, j))
        return -(self.Lx(i, j, p) + self.Ly(i, j, p)) + self.Dx(i, j, p) + self.Dy(i, j, p) - self.get_grid_func(self.M.f, i, j)

    def Au(self, p):
        res = np.zeros((self.Nx, self.Ny))
        for i in range(1, self.Nx - 1):
            for j in range(1, self.Ny - 1):
                res[i, j] = self.A(i, j, p)
        return res

    def dA(self, x, w, h = 1e-8):
        if np.linalg.norm(x) != 0 and np.linalg.norm(w) != 0:
            tmp = h * np.linalg.norm(x) / np.linalg.norm(w)
            return (self.Au(x + tmp * w) - self.Au(x)) / tmp

        if np.linalg.norm(x) < 1e-10 and np.linalg.norm(w) != 0:
            tmp = h / np.linalg.norm(w)
            return (self.Au(tmp * w) - self.Au(np.zeros_like(x))) / tmp

        return np.zeros_like(w)



    def sc_mult(self, u, v):
        s = 0
        for i in range(1, self.Nx - 1):
            for j in range(1, self.Ny - 1):
                s += u[i, j] * v[i, j]
        return s

    def solveBiCG(self, start ,b, tol=1e-3, max_time=100, max_iter=10000000):
        res = start

        start_time = time.time()

        st = self.dA(self.p, start)
        r0 = np.zeros((self.Nx, self.Ny))
        for i in range(1, self.Nx - 1):
            for j in range(1, self.Ny - 1):
                r0[i, j] = b[i][j] - st[i][j]

        r = r0.copy()
        rho_old = alpha = omega = 1.0
        v = np.zeros_like(r0)
        p = np.zeros_like(r0)

        iter_count = 0

        while iter_count < max_iter and (time.time() - start_time) < max_time:
            rho_new = self.sc_mult(r0, r)
            if abs(rho_new) < 1e-10:
                print("Прерывание: rho слишком мал.")
                break
            if iter_count == 0:
                p = r.copy()
            else:
                beta = (rho_new / rho_old) * (alpha / omega)
                p = r + beta * (p - omega * v)

            v = self.dA(self.p, p)
            alpha = rho_new / self.sc_mult(r0, v)

            s = r - alpha * v

            if np.linalg.norm(s) < tol:
                res += alpha * p
                print(f"Сошелся за {iter_count} итераций")
                break

            t = self.dA(self.p, s)
            omega = self.sc_mult(t, s) / self.sc_mult(t, t)

            res += alpha * p + omega * s
            r = s - omega * t

            if np.linalg.norm(r) < tol:
                print(f"Сошелся за {iter_count} итераций")
                break

            rho_old = rho_new
            iter_count += 1

        return res

    def solve(self):
        self.init(self.p)

        tmp = np.ones((self.Nx, self.Ny), dtype='double')
        for i in range(self.Nx):
            tmp[i][0] = 0.
            tmp[i][-1] = 0.
        for j in range(self.Ny):
            tmp[0][j] = 0.
            tmp[-1][j] = 0.

        delta = self.solveBiCG(tmp, -self.Au(self.p))
        self.p += delta
        while np.linalg.norm(delta)> 1e-2:
            print(np.linalg.norm(delta))
            delta = self.solveBiCG(delta, -self.Au(self.p))
            self.p += delta
        return self.p

    def get_r_norm(self):
        if not hasattr(self.M, 'u_an'):
            return -1.
        s = 0
        for i in range(1, self.Nx - 1):
            for j in range(1, self.Ny - 1):
                s+=(self.p[i, j] - self.get_grid_func(self.M.u_an, i, j))**2
        return round_to_significant_figures(np.sqrt(s), 1)

    def plot_heatmap(self):
        """
        Построение тепловой карты для решения
        """
        plt.figure(figsize=(8, 6))
        plt.imshow(self.p.T, extent=[0, self.M.X, 0, self.M.Y], origin='lower', cmap='inferno', aspect='auto')
        plt.colorbar(label='Температура')
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title(f'Норма невязки: {self.get_r_norm()}')
        # output_path = os.path.join('out_im_bi', 'heatmap_' + str(self.Nx) +'_'+ str(self.M.TaskNumber) +'.png')
        # plt.savefig(output_path)
        plt.show()

    def do_all(self):
        self.solve()
        self.plot_heatmap()