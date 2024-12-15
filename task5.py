import numpy as np

TaskNumber = 5

X = 0.5
Y = 0.5


def u_an(x, y):
    return x**2 + y**2

def f(x, y):
    return -6*(x**2+y**2)

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
    return x

def v2(x, y):
    return y

def k1(x, y, u):
    return u

def k2(x, y, u):
    return u