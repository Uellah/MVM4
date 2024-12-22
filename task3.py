import numpy as np

TaskNumber = 3

X = 1
Y = 1


def u_an(x, y):
    return x + y**2

def f(x, y):
    return -(1 + 2*(x+3*y**2))

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
    return 0

def v2(x, y):
    return 0

def k1(x, y, u):
    return u

def k2(x, y, u):
    return u