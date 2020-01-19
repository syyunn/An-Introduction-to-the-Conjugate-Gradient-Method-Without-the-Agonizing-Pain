import numpy as np

from nptyping import Array

# Constants to be used
x = np.mat([[-6.0], [6.0]])
A = np.mat([[3.0, 2.0], [2.0, 6.0]])
b = np.mat([[2.0], [-8.0]])
c = 0.0

# Types to be used
dim = 2
type_x = Array[float, dim, 1]
type_A = Array[float, dim, dim]
type_b = Array[float, dim, 1]
type_c = float

if __name__ == "__main__":
    pass
