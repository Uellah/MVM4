import numpy as np

TaskNumber = 6

X = 2
Y = 2


def u_an(x, y):
    return np.cos(x) + np.sin(y) + 1

def f(x, y):
    return -2 * np.cos(x) * np.sin(y) + x * np.sin(x) - y * np.cos(y)

def g_l(x, y):
    return u_an(0, y)

def g_r(x, y):
    return u_an(X, y)

def g_down(x, y):
    return u_an(x, 0)

def g_up(x, y):
    return u_an(x, Y)

def v1(x, y):
    return -x

def v2(x, y):
    return -y

def k1(x, y, u):
    return u

def k2(x, y, u):
    return u
