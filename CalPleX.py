from math import pi, sqrt
import matplotlib.pyplot as plt
import numpy as np

class Calculator:
    def __init__(self, a, b):
        self.num1 = a
        self.num2 = b

    def add(self):
        return self.num1 + self.num2

    def subtract(self):
        return self.num1 - self.num2

    def multiply(self):
        return self.num1 * self.num2

    def divide(self):
        return self.num1 / self.num2


class AvgCal:
    def __init__(self, data):
        self.data = data
        self.quantity = len(data)

    def calculate(self):
        data_sum = 0
        for data in self.data:
            data_sum = data_sum + data
        return data_sum / self.quantity


class PercentCal:
    def __init__(self, whole, part):
        self.whole = whole
        self.part = part

    def calculate(self):
        return self.part / self.whole * 100


class LinearGrapher:
    def __init__(self, coef, inter):
        self.coef = coef
        self.inter = inter

    def graph(self, a, b):
        x = np.arange(a, b+1)
        y = self.coef * x + self.inter
        plt.plot(x, y)
        plt.grid(True)
        plt.show()


class QuadrGrapher:
    def __init__(self, coef1, coef2, inter):
        self.coef1 = coef1
        self.coef2 = coef2
        self.inter = inter

    def graph(self, a, b):
        x = np.arange(a, b+1, 0.1)
        y = self.coef1 * (x**2) + self.coef2 * x + self.inter
        plt.plot(x, y)
        plt.grid(True)
        plt.show()


# Area of triangles, quadrilaterals
def square_a(s):
    return s**2


def rect_a(l, w):
    return l * w


def trap_a(b1, b2, h):
    return ((b1 + b2) * h) / 2


def kite_a(d1, d2):
    return d1 * d2 / 2


def rhom_a(d1, d2):
    return d1 * d2 / 2


def tri_a(l, w):
    return l * w / 2


# Perimeter of polygons
def tri_p(s1, s2, s3):
    return s1 + s2 + s3


def quadr_p(s1, s2, s3, s4):
    return s1 + s2 + s3 + s4


def pent_p(s1, s2, s3, s4, s5):
    return s1 + s2 + s3 + s4 + s5


def hex_p(s1, s2, s3, s4, s5, s6):
    return s1 + s2 + s3 + s4 + s5 + s6


# Area of circle
def circ_a(r):
    return r ** 2 * pi


# Diameter of a circle
def circ_d(r):
    return r * 2 * pi


# Volume of pyramids & cones
def pyramid_v(b, h):
    return b * h / 3


# Volume of prisms & cylinders
def prism_v(b, h):
    return b * h


# Pythagorean Theorem
def pytha_theo(a, b):
    return sqrt(a**2 + b**2)


# Factorial
def factorial(a):
    if a == 1:
        return 1
    return a * factorial(a-1)