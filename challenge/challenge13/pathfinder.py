from numpy.lib.arraysetops import isin
from challenge import functions

class PathFinder:
    
    def __init__(self, startNode, tMap):
        self.bestFound = None # lowest amount of steps found to reach goal
        self.totalProcesses = 0 # debugging

        self.successfulPath = None

        self.find(startNode, -1, [], [])
        
    # worse means step count is higher than node's count
    def stepCountWorse(self, stepCount, node):
        return (node.crMnStp != None and node.crMnStp <= stepCount) or (self.bestFound != None and self.bestFound <= stepCount)

    def find(self, node, stepCount, path):
        
        #path = pathOld.copy()
        self.totalProcesses += 1 # debugging
        stepCount += 1
        
        currentStepCountWorse = self.stepCountWorse(stepCount, node)


        if currentStepCountWorse: # if pathfinder is in a worse position, early return
            return
        
        node.crMnStp = functions.minWithNone(node.crMnStp, stepCount)
        
        if node.isGoal:
            #print(f"Goal found: {stepCount}\tPath length: {len(path)}")
            if functions.minWithNone(stepCount, self.bestFound) == stepCount:
                #print(f"Path set with length {stepCount}")
                self.successfulPath = path
            self.bestFound = functions.minWithNone(stepCount, self.bestFound)
            return

        # #if self.tMap.getNode(node.i, node.j).char == " " or self.tMap.getNode(node.i, node.j).char == "*":
        # self.tMap.getNode(node.i, node.j).char = "O" # debugging
        # input("") # debugging
        # print(self.tMap) # debugging
        # print(f"stepCount: {stepCount} (worse:{currentStepCountWorse})\ttorchLeft: {torchLeft} (worse:{currentTorchLeftWorse})\n")
        # if self.tMap.getNode(node.i, node.j).char == "O":
        #     self.tMap.getNode(node.i, node.j).char = " " # debugging

        for connectedNode in node.connections:
            path.append(connectedNode)
            pathNew = path.copy()
            path.pop(-1)
            
            #print(f"stepCount: {stepCount}\tpos: {node.char}[{node.j}, {node.i}] -> {connectedNode.char}[{connectedNode.j}, {connectedNode.i}]") # debugging
            self.find(connectedNode, stepCount, pathNew)


def main():
    pass
