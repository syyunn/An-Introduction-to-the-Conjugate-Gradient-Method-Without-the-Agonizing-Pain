import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

from Constants import *
import quadratic


def bowl(A, b, c):
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
    plt.figure(figsize=(6, 6))
    cp = plt.contour(x1, x2, zs, 20)
    plt.clabel(cp, inline=1, fontsize=10)
    plt.show()


if __name__ == "__main__":
    # figure1(A, b)
    x1, x2, zs = figure2(A, b, c)
    figure3(x1, x2, zs)
    pass
