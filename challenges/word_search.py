import random
import numpy as np

rows = 10
cols = 10

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
    word = wordBank[random.randint(0, len(wordBank) - 1)]
    # return word
    return "test"

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


def insertWord(wordMatrix):
    word = getRandomWord()
    direction = 1#random.randint(1, 3)  # horizontal: 1, vertical: 2, diagonal: 3
    if direction == 1:    # Horizontal
        while len(word) > cols:
            word = getRandomWord()
        print(word)
        rowStart = random.randint(0, len(wordMatrix) - 1)
        colStart = random.randint(0, len(wordMatrix[rowStart]) - len(word))
        for letter in word:
            wordMatrix[rowStart][colStart] = letter
            colStart += 1
    elif direction == 2:  # Vertical
        while len(word) > rows:
            word = getRandomWord()
        print(word)
        rowStart = random.randint(0, len(wordMatrix) - len(word))
        colStart = random.randint(0, len(wordMatrix[rowStart]) - 1)
        for letter in word:
            wordMatrix[rowStart][colStart] = letter
            rowStart += 1
    else:                 # Diagonal
        while len(word) > rows or len(word) > cols:
            word = getRandomWord
        print(word)
        colStart = random.randint(0, len(wordMatrix) - len(word))
        rowStart = random.randint(0, len(wordMatrix[colStart]) - len(word))
        for letter in word:
            wordMatrix[colStart][rowStart] = letter
            rowStart += 1
            colStart += 1

def letterCheck(direction, wordMatrix, word):  # tests all possible positions if word will work there ******NEED TO RENAME********
    checkList = np.ones((rows, cols), dtype=int)
    if direction == 1:
        for idxi, i in enumerate(checkList):
            for idxj, j in enumerate(i):
                for idxl, letter in enumerate(word):
                    try:
                        # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi][idxj + idxl] == "" or wordMatrix[idxi][idxj + idxl] == letter:
                            pass
                        else:
                            checkList[idxi][idxj + idxl] = 0
                    except IndexError:
                        checkList[idxi][idxj] = 0
    return checkList



wordList = initMatrix(rows, cols)

insertWord(wordList)

printMatrix(letterCheck(1, wordList, getRandomWord()))  # returns one false negative, need to investigate
wordList = randLetterMatrix(wordList)

printMatrix(wordList)
