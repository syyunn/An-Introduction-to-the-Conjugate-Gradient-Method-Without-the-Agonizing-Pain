from unittest import TestCase

from Constants import *
import quadratic


class TestSuite(TestCase):
    def test_quadratic_function(self):
        quadratic.f(x, A, b, c)

    def test_quadratics_derivative(self):
        quadratic.f_derivative(x, A, b)
