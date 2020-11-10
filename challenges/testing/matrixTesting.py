import numpy as np

def posMatrix():
    matrix = np.empty((5,5), dtype=np.dtype('U6'))
    i = 0
    for i in range(5):
        j = 0
        for j in range(5):
            matrix[i][j] = f"({i},{j})"
            j += 1
        i += 1
    return matrix

print(posMatrix())
