import numpy as np
from node import Node
import functions

def stringToNodeMatrix(text):
    lines = text.splitlines()

    matrix = np.zeros([len(lines), len(lines[0])], dtype=np.object)

    for i, line in enumerate(lines):
        for j, char in enumerate(line):
            matrix[i][j] = Node(char, [i, j])
    return matrix
    

class MapParser:
    def parse(file):
        # print("parsing")

        file = open(file, "r").read()
        
        matrix = stringToNodeMatrix(file)

        return matrix
