import numpy as np

start = """20,20
0,10 10,20
20,9 10,20
0,0 20,9
4,13 6,15
14,15 16,13
3,6 4,8
4,5 5,7
5,4 6,6
6,4 7,5
6,4 14,3
13,4 15,5
14,5 16,6
15,6 17,7
17,8 16,7
0,9 10,10
0,20, 20,0
0,0 20,1
0,19, 20,20
0,1 1,19
19,1 20,19
"""

def matrixString(mat) -> str:
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    return out

start = start.splitlines()
for idx, piece in enumerate(start):
    start[idx] = piece.split(" ")
    for idxi, subpiece in enumerate(start[idx]):
        start[idx][idxi] = subpiece.split(",")
        for idxj, subsubpiece in enumerate(start[idx][idxi]):
            try:    
                start[idx][idxi][idxj] = int(subsubpiece)
            except ValueError:
                print("fail")


print(start)


def rectangleMaker(matrix, xs, ys):
    xs.sort()
    ys.sort()
    x1, x2 = xs
    y1, y2 = ys
    for i, row in enumerate(matrix[x1:x2]):
        for j in range(len(row[y1:y2])):
            if matrix[i+ x1][j + y1] == ' ':
                matrix[i+ x1][j + y1] = '*'
            else:
                matrix[i+ x1][j + y1] = ' '

def mapParser(start, matrix):
    for i, line in enumerate(start):
        if i == 0:
            continue
        for coord in line:
            x, y = coord[:2]
        x1 = line[0][0]
        y1 = line[0][1]
        x2 = line[1][0]
        y2 = line[1][1]
        rectangleMaker(matrix, [x1, x2], [y1, y2])

def main():
    x = start[0][0][0]
    y = start[0][0][1]
    canvas = np.full((x,y), ' ', dtype=np.str)

    mapParser(start, canvas)

    canvas = np.rot90(canvas, axes=(0, 1))
    print(matrixString(canvas))

main()