import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

from Constants import *
import quadratic


def figure1(A, b):
    """Plot linear systems of equations defined over 2 dimensional input"""
    plt.figure(figsize=(10, 8))

    # Set x-axis range
    plt.xlim((-4, 6))
    # Set y-axis range
    plt.ylim((-6, 4))

    x = np.linspace(-4, 6)

    y1 = (np.array(A)[0, 0] * x - np.array(b)[0, 0]) / -np.array(A)[0, 1]
    plt.plot(x, y1, color="black")

    y2 = (np.array(A)[1, 0] * x - np.array(b)[1, 0]) / -np.array(A)[1, 1]
    plt.plot(x, y2, color="black")

    plt.plot([-4, 6], [0, 0], color="C0")
    plt.plot([0, 0], [-6, 4], color="C0")
    plt.grid()

    plt.text(0.75, 1, "3x1 + 2x2 = 2")
    plt.text(4, -2, "2x1 + 6x2 = -8")

    plt.show()
    return None


def figure2(A, b, c):
    """Plot quadratic(z-axis) value over 2-dimensional input domain
    Since default A is positive-definite, its shape is paraboloid bowl."""
    fig = plt.figure(figsize=(10, 8))
    qf = fig.gca(projection="3d")  # '3d' requires "from mpl_toolkits.mplot3d
    # import Axes3D"
    size = 20
    x1 = list(np.linspace(-6, 6, size))
    x2 = list(np.linspace(-6, 6, size))
    x1, x2 = np.meshgrid(x1, x2)
    zs = np.zeros((size, size))
    for i in range(size):
        for j in range(size):
            x = np.mat([[x1[i, j]], [x2[i, j]]])
            zs[i, j] = quadratic.f(x, A, b, c)
    qf.plot_surface(x1, x2, zs, rstride=1, cstride=1, cmap=cm.coolwarm, linewidth=0)
    # plt.show()
    return x1, x2, zs


def figure3(x1, x2, zs):
    """Plot quadratics' contour map"""
    plt.figure(figsize=(6, 6))
    cp = plt.contour(x1, x2, zs, 20)
    plt.clabel(cp, inline=1, fontsize=10)
    plt.show()


def figure4():
    """Plot 1st-order derivatives' quiver"""
    # Default Configure ####################
    plt.figure(figsize=(10, 8))
    # Set x-axis range
    plt.xlim((-4, 6))
    # Set y-axis range
    plt.ylim((-8, 6))

    plt.plot([-4, 6], [0, 0], color="black")
    plt.plot([0, 0], [-8, 6], color="black")
    ########################################

    size = 13
    x1 = list(np.linspace(-4, 6, size))
    x2 = list(np.linspace(-8, 6, size))
    x1, x2 = np.meshgrid(x1, x2)
    zs = np.zeros((size, size, 2))
    for i in range(size):
        for j in range(size):
            x = np.mat([[x1[i, j]], [x2[i, j]]])
            zs[i, j, 0] = np.asarray(quadratic.f_derivative(x, A, b))[0][0]
            zs[i, j, 1] = np.asarray(quadratic.f_derivative(x, A, b))[1][0]
    plt.quiver(x1, x2, zs[:, :, 0], zs[:, :, 1])

    plt.show()


if __name__ == "__main__":
    # figure1(A, b)
    # x1, x2, zs = figure2(A, b, c)
    # figure3(x1, x2, zs)
    figure4()
    pass



