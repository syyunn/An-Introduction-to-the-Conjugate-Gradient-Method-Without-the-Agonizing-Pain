import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

from Constants import *
import quadratic


def figure2(A, b, c):
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
    plt.show()
    # The minimum point of this surface is the solution to Ax = b
    return x1, x2, zs


if __name__ == "__main__":
    x1, x2, zs = figure2(A, b, c)
    pass
