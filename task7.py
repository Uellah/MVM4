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

X = 4*pi
Y = 4*pi

def u_an(x, y):
    """Аналитическое решение"""
    return cos(x) + sin(y)

def f(x, y):
    # Пересчет правой части с учетом новых k1 и k2
    term1 = (cos(x)+sin(y))*(sin(x)*(-2*sin(x)*x+cos(x)+sin(y))+(cos(x)+sin(y))*x*cos(x))
    term2 = (-(cos(x)+sin(y))*(cos(y)*(2*cos(y)*y+cos(x)+sin(y))-(cos(x)+sin(y))*y*sin(y)))
    term3 = (-y*cos(y))
    term4 = x*sin(x)

    return term1 + term2 + term3 + term4

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
    return -x

def v2(x, y):
    """Скорость v2"""
    return -y

def k1(x, y, u):
    """Коэффициент k1"""
    return u**2 * x

def k2(x, y, u):
    """Коэффициент k2"""
    return u**2 * y