import matplotlib.pyplot as plt
import matplotlib.cm as cm
from mpl_toolkits.mplot3d import Axes3D

from Constants import *
import quadratic


def figure1(A, b):
    plt.figure(figsize=(10, 8))

    # Set x-axis range
    plt.xlim((-4, 6))
    # Set y-axis range
    plt.ylim((-6, 4))

    x = np.linspace(-4, 6)

    y1 = (np.array(A)[0, 0] * x - np.array(b)[0, 0]) / -np.array(A)[0, 1]
    plt.plot(x, y1, color='black')

    y2 = (np.array(A)[1, 0] * x - np.array(b)[1, 0]) / -np.array(A)[1, 1]
    plt.plot(x, y2, color='black')

    plt.plot([-4, 6], [0, 0], color='C0')
    plt.plot([0, 0], [-6, 4], color='C0')
    plt.grid()

    plt.text(0.75, 1, "3x1 + 2x2 = 2")
    plt.text(4, -2, "2x1 + 6x2 = -8")

    plt.show()
    return None


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
    return x1, x2, zs


if __name__ == "__main__":
    figure1(A, b)
    # figure2(A, b, c)
    pass



