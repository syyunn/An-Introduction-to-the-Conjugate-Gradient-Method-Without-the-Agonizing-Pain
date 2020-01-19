from unittest import TestCase

import numpy as np

import quadratic


class TestSuite(TestCase):
    def test_quadratic_function(self):
        x = np.mat([[-6.0], [6.0]])
        A = np.mat([[3.0, 2.0], [2.0, 6.0]])
        b = np.mat([[2.0], [-8.0]])
        c = 0.0
        quadratic.f(x, A, b, c)
