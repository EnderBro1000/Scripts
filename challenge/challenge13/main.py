from pathfinder import PathFinder
from tMap import TMap
from node import Node
import sys
import time
#import resource

def main():
    tStart = time.time()
    # print(sys.getrecursionlimit())
    # resource.setrlimit(resource.RLIMIT_STACK, [0x10000000, resource.RLIM_INFINITY])
    sys.setrecursionlimit(0x100000)
    # print(sys.getrecursionlimit())
    tMap = TMap("inputMaps\\Prob16Corner.test.txt")
    # tMap = TMap("inputMaps\\judge\\Prob16.in.txt")
    pathfinder = PathFinder(tMap.startNode, tMap)

    tFinish = time.time()
    tDif = (tFinish - tStart) * 1000 # execution time in ms

    # print(len(pathfinder.successfulPath)) # debugging
    for node in pathfinder.successfulPath: # debugging
        if node.char == " ": # debugging
            node.char = "O" # debugging
    print(tMap) # debugging

    print(f"\n\tsolution: {pathfinder.bestFound}\tInstances: {pathfinder.totalProcesses}")
    print(f"\texecution time: {round(tDif, 3)} ms")

main()
