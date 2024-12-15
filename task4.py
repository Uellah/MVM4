import numpy as np

TaskNumber = 4

X = 4
Y = 4


def u_an(x, y):
    return np.sin(np.pi*x)

def f(x, y):
    return np.pi**2*np.sin(np.pi*x)

# лишние переменные обьявлены для универсальности реализации получения сеточной аппроксимации
def g_l(x, y):
    return u_an(0, y)

def g_r(x, y):
    return u_an(X, y)

def g_down(x, y):
    return u_an(x, 0)

def g_up(x, y):
    return u_an(x, Y)

def v1(x, y):
    return 0.

def v2(x, y):
    return 0.

def k1(x, y, u):
    return 1.

def k2(x, y, u):
    return u