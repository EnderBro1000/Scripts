from mapParser import MapParser
from node import Node
import functions

class TMap:
    def __init__(self, inputFile):
        self.inputFile = inputFile

        self.startNode = None
        # print("created map")
        self.nodeMatrix = MapParser.parse(inputFile)

        # self.nodeMatrix = np.flip(self.nodeMatrix)

        for i, rows in enumerate(self.nodeMatrix): ### # [1:-1]??????hlp????????????
            for j, node in enumerate(rows):
                if (node.isStart):
                    self.startNode = node
                if not node.isWall:
                    node.addOpenConnection(self.nodeMatrix[i][j-1]) # up
                    node.addOpenConnection(self.nodeMatrix[i-1][j]) # left
                    node.addOpenConnection(self.nodeMatrix[i][j+1]) # down
                    node.addOpenConnection(self.nodeMatrix[i+1][j]) # right

    def getNode(self, i, j):
        return self.nodeMatrix[i][j]


    def __repr__(self) -> str:
        return functions.matrixString(self.nodeMatrix)
                

def main():
    # tMap = TMap("inputMaps/examples/Prob16.in.txt")
    tMap = TMap("inputMaps/mapTest.txt")
    
    print(tMap)
    print("Connections: ")
    print(Node.outAllConnections(tMap.nodeMatrix))
    

