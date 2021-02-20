import numpy as np

matrix = np.full((8,8), "000000")

def matrix_references(matrix):
    for idxi, i in enumerate(matrix):
        for idxj, j in enumerate(i):
            matrix[idxi][idxj] = f"({idxi}, {idxj})"
    return matrix

def matrix_coords(matrix):
    for idxi, i in enumerate(np.flip(matrix)):
        for idxj, j in enumerate(np.flip(i)):
            matrix[idxi][idxj] = f"({idxi}, {idxj})"
    return matrix

def printCoordMatrix(mat):
    mat = np.flip(mat, 1)
    out = ""
    for idxi, i in enumerate(mat):
        for idxj, j in enumerate(i):
            out += f"{mat[idxj][idxi]} "
        out += "\n"
    print(out)

printCoordMatrix(matrix_references(matrix))