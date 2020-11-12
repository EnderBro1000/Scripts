import random
import numpy as np

rows = 10
cols = 10

wordBank = [
    "TEST", "AMUSEMENT", "APPLES", "AUTUMN", "BATS", "BLACK", "BOO", "CANDY", "CAT"#,
    # "COSTUMES", "DRACULA",	"EERIE"," EXCITEMENT", "FRANKENSTEIN", "FRIGHTEN",
    # "GAMES", "GHOSTS", "GOBLIN", "HALLOWEEN", "HARVEST", "HAYRIDE", "MASK",
    # "MONSTER", "MUMMY", "NIGHT", "OCTOBER", "ORANGE", "PARTY", "PRANK", "PUMPKINS",
    # "SAFE", "SCARE", "SHADOWS", "SKELETON", "SPIDER", "SPOOKY", "TRICKORTREAT", "WITCH"
]

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def getRandomLetter():
    # return letters[random.randint(0, len(letters) - 1)]
    return "0"

def getWord():
    random.shuffle(wordBank)
    try:
        word = wordBank.pop(1)
    except IndexError:
        return None
    return word

def printMatrix(mat):
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    print(out)

def initMatrix(xLength, yLength):
    return np.zeros((xLength, yLength), dtype=str)

def randLetterMatrix(wordMatrix):  # Randomizes
    # pos = 0
    for i in range(len(wordMatrix)):
        for j in range(len(wordMatrix[0])):
            if wordMatrix[i][j] == "":
                wordMatrix[i][j] = getRandomLetter()
                # wordMatrix[i][j] = pos
                # pos += 1
    return wordMatrix

def wordCheck(direction, wordMatrix, word):  # tests all possible positions if word will work there
    print(word)
    possible = False
    printMatrix(wordMatrix)
    checkMatrix = np.ones((rows, cols), dtype=int)
    if direction == 1:
        for idxi, i in enumerate(checkMatrix):
            for idxj, j in enumerate(i):
                for idxl, letter in enumerate(word):
                    try:
                        # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi][idxj + idxl] == "0" or wordMatrix[idxi][idxj + idxl] == letter:
                            possible = True
                        else:
                            checkMatrix[idxi][idxj] = 0
                    except IndexError:
                        checkMatrix[idxi][idxj] = 0
    if direction == 2:
        for idxi, i in enumerate(checkMatrix):
            for idxj, j in enumerate(i):
                for idxl, letter in enumerate(word):
                    try:
                        # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi + idxl][idxj] == "0" or wordMatrix[idxi + idxl][idxj] == letter:
                            possible = True
                        else:
                            checkMatrix[idxi][idxj] = 0
                    except IndexError:
                        checkMatrix[idxi][idxj] = 0
    else:
        for idxi, i in enumerate(checkMatrix):
            for idxj, j in enumerate(i):
                for idxl, letter in enumerate(word):
                    try:
                        # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi + idxl][idxj + idxl] == "0" or wordMatrix[idxi + idxl][idxj + idxl] == letter:
                            possible = True
                        else:
                            checkMatrix[idxi][idxj] = 0
                    except IndexError:
                        checkMatrix[idxi][idxj] = 0
    return checkMatrix, possible

def insertWord(wordMatrix):
    word = getWord()
    if word is None:
        return wordMatrix
    directions = (list(range(1, 4)))
    random.shuffle(directions)
    print(directions)  # horizontal: 1, vertical: 2, diagonal: 3
    try:
        direction = directions.pop(0)
    except IndexError:
        return wordMatrix
    checkMatrix = wordCheck(direction, wordMatrix, word)
    for direction in directions:
        if checkMatrix[1] == False:
            word = getWord()
            if word is None:
                return wordMatrix
            checkMatrix = wordCheck(direction, wordMatrix, word)
    if checkMatrix[1] == False:
        return wordMatrix
    if direction == 1:    # Horizontal
        while checkMatrix:
            word = getWord()
        print(word)
        rowStart = random.randint(0, len(wordMatrix) - 1)
        colStart = random.randint(0, len(wordMatrix[rowStart]) - len(word))
        for letter in word:
            wordMatrix[rowStart][colStart] = letter
            colStart += 1
    elif direction == 2:  # Vertical
        while len(word) > rows:
            word = getWord()
        print(word)
        rowStart = random.randint(0, len(wordMatrix) - len(word))
        colStart = random.randint(0, len(wordMatrix[rowStart]) - 1)
        for letter in word:
            wordMatrix[rowStart][colStart] = letter
            rowStart += 1
    else:                 # Diagonal
        while len(word) > rows or len(word) > cols:
            word = getWord
        print(word)
        colStart = random.randint(0, len(wordMatrix) - len(word))
        rowStart = random.randint(0, len(wordMatrix[colStart]) - len(word))
        for letter in word:
            wordMatrix[colStart][rowStart] = letter
            rowStart += 1
            colStart += 1
    return wordMatrix




wordList = initMatrix(rows, cols)
while len(wordBank) > 0:
    wordList = insertWord(wordList)

wordList = randLetterMatrix(wordList)

print(wordList)
printMatrix(wordList)

# There seems to be an infinite loop somewhere, need to find it later
