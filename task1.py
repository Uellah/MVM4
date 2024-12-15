import numpy as np

TaskNumber = 1

X = 0.5
Y = 0.5


def u_an(x, y):
    return 1.

def f(x, y):
    return 0

# лишние переменные обьявлены для универсальности реализации получения сеточной аппроксимации
def g_l(x, y):
    return 100.

def g_r(x, y):
    return 100.

def g_down(x, y):
    return 100.

def g_up(x, y):
    return 100.

def v1(x, y):
    return 0

def v2(x, y):
    return 0

def k(x, y, u):
    return 1.
