import random

rows = 5
cols = 5

wordBank = [
    "TEST", "AMUSEMENT", "APPLES", "AUTUMN", "BATS", "BLACK", "BOO", "CANDY", "CAT",
    "COSTUMES", "DRACULA",	"EERIE"," EXCITEMENT", "FRANKENSTEIN", "FRIGHTEN",
    "GAMES", "GHOSTS", "GOBLIN", "HALLOWEEN", "HARVEST", "HAYRIDE", "MASK",
    "MONSTER", "MUMMY", "NIGHT", "OCTOBER", "ORANGE", "PARTY", "PRANK", "PUMPKINS",
    "SAFE", "SCARE", "SHADOWS", "SKELETON", "SPIDER", "SPOOKY", "TRICKORTREAT", "WITCH"
]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getRandomLetter():
    return letters[random.randint(0, len(letters) - 1)]

def getRandomWord():
    # return wordBank[random.randint(0, wordBank.len)]
    return wordBank[0]

def printMatrix(mat):
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    print(out)

def initWordList(xLength, yLength):
    wordList = [[0] * xLength] * yLength  
    for i in range(xLength):
        for j in range(yLength):
            # wordList[i] = 
            # wordList.append()
            wordList[i][j] = getRandomLetter()
            print(f"i: {i}, j: {j}, letter: {wordList[i][j]}")
        print(f"\nrow: {i}\t{wordList[i]}")
        printMatrix(wordList)
    return wordList




def insertWords(wordList):
    # if (wordList.len < word)
    start = 0
    word = getRandomWord()
    i = 0
    while i != len(word):
        i += 1
        # print(i)
    
# wordList = initWordList(rows, cols)

# insertWords(wordList)

# print(wordList)
# printMatrix(wordList)




def initLetterArray(xLength, yLength):
    array = [[0] * xLength] * yLength  # Creates blank array
    rowPos = 0
    for row in array:
        colPos = 0
        for col in row:
            array[rowPos][colPos] = f"({rowPos}, {colPos})"
            print(array)
            colPos += 1
        rowPos += 1
    printMatrix(array)

initLetterArray(5, 5)