import numpy as np

TaskNumber = 2

X = 0.5
Y = 0.5


def u_an(x, y):
    return x + y

def f(x, y):
    return x + y - 2

# лишние переменные обьявлены для универсальности реализации получения сеточной аппроксимации
def g_l(x, y):
    return y

def g_r(x, y):
    return X + y

def g_down(x, y):
    return x

def g_up(x, y):
    return Y + x

def v1(x, y):
    return x

def v2(x, y):
    return y

def k1(x, y, u):
    return u

def k2(x, y, u):
    return 1.