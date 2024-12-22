# import numpy as np
#
# TaskNumber = 4
#
# X = 1
# Y = 1
#
# # Зададим аналитическое решение как функцию Розенброка
# def u_an(x, y):
#     return (1 - x)**2 + 100 * (y - x**2)**2
#
# # Подставим аналитическое решение в уравнение, чтобы получить f(x, y)
# def f(x, y):
#     dx2 = -400 * x * (y - x**2) - 2 * (1 - x)
#     dy2 = 200 * (y - x**2)
#     return dx2 + dy2
#
# # Граничные условия для всех сторон области
# def g_l(x, y):
#     return u_an(0, y)
#
# def g_r(x, y):
#     return u_an(X, y)
#
# def g_down(x, y):
#     return u_an(x, 0)
#
# def g_up(x, y):
#     return u_an(x, Y)
#
# # Поля скорости
# def v1(x, y):
#     return -x
#
# def v2(x, y):
#     return -y
#
# # Коэффициенты диффузии
# def k1(x, y, u):
#     return u
#
# def k2(x, y, u):
#     return u


from numpy import sin, cos, pi

TaskNumber = 7

X = 2.5
Y = 2.5

def u_an(x, y):
    """Аналитическое решение"""
    return sin(pi*x)*sin(pi*y)

def f(x, y):
    return -pi**2*sin(pi*x)*sin(pi*y)*((sin(pi*y))**2*(2*(cos(pi*x))**2-(sin(pi*x))**2)+(sin(pi*x))**2*(2*(cos(pi*y))**2-(sin(pi*y))**2))

def g_l(x, y):
    """Граничное условие слева"""
    return u_an(0, y)

def g_r(x, y):
    """Граничное условие справа"""
    return u_an(X, y)

def g_down(x, y):
    """Граничное условие снизу"""
    return u_an(x, 0)

def g_up(x, y):
    """Граничное условие сверху"""
    return u_an(x, Y)

def v1(x, y):
    """Скорость v1"""
    return 0

def v2(x, y):
    """Скорость v2"""
    return 0

def k1(x, y, u):
    """Коэффициент k1"""
    return u**2

def k2(x, y, u):
    """Коэффициент k2"""
    return u**2