def minWithNone(a, b): # returns the min between a and b, or whichever is not None
    if a is None:
        return b
    elif b is None:
        return a
    return min(a,b)
    
def maxWithNone(a, b): # returns the max between a and b, or whichever is not None
    if a is None:
        return b
    elif b is None:
        return a
    return max(a,b)

def matrixString(mat) -> str:
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    return out

def stringToNodeMatrix(text):
    lines = text.splitlines()

    matrix = np.zeros([len(lines), len(lines[0])], dtype=np.object)

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix[i][j] = Node(char, [i, j])
    return matrix