import pretty_errors
import random
import numpy as np

rows = 8
cols = 8

wordBank = [
    "AMUSEMENT", "AUTUMN", "APPLES", "BLACK", "CANDY", "BATS", "TEST", "BOO", "CAT"#,
    # "COSTUMES", "DRACULA",	"EERIE"," EXCITEMENT", "FRANKENSTEIN", "FRIGHTEN",
    # "GAMES", "GHOSTS", "GOBLIN", "HALLOWEEN", "HARVEST", "HAYRIDE", "MASK",
    # "MONSTER", "MUMMY", "NIGHT", "OCTOBER", "ORANGE", "PARTY", "PRANK", "PUMPKINS",
    # "SAFE", "SCARE", "SHADOWS", "SKELETON", "SPIDER", "SPOOKY", "TRICKORTREAT", "WITCH"
]
tempWordBank = wordBank

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"



def printMatrix(mat):
    out = ""
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            out += f"{mat[i][j]} "
        out += "\n"
    print(out)


def initMatrix(xLength, yLength):
    return np.zeros((xLength, yLength), dtype=str)

def getRandomLetter():
    # return letters[random.randint(0, len(letters) - 1)]
    return "0"

def getWord(wordMatrix):
    if len(tempWordBank > 1):
        word = tempWordBank.pop()
    else:
        return None
    direction, directions = randomDirection(wordMatrix, word)

    if directions < 1:
        getWord(wordMatrix)
    possible = 0:
    while possible < 1:
        possible = len(wordCheck(direction, word, wordMatrix))
        direction, directions = randomDirection(wordMatrix, word) #writing HERE ******************************************
    else: 


def randLetterMatrix(wordMatrix):
    for idxi, i in enumerate(wordMatrix):
        for idxj, j in enumerate(i):
            if wordMatrix[idxi][idxj] == "":
                wordMatrix[idxi][idxj] = getRandomLetter()
    return wordMatrix

def wordCheck(direction, word, wordMatrix):
    checkList = set()
    for idxi, i in enumerate(wordMatrix):
        for idxj, j in enumerate(i):
            possible = True
            for idxl, letter in enumerate(word):
                if direction == 1:
                    try:
                        if np.all(wordMatrix[idxi][idxj + idxl] != "" and wordMatrix[idxi][idxj + idxl] != letter):
                            possible = False
                    except IndexError:
                        possible = False
                        break
                elif direction == 2:
                    try:
                        if np.all(wordMatrix[idxi + idxl][idxj] != "" and wordMatrix[idxi + idxl][idxj] != letter):
                            possible = False
                    except IndexError:
                        possible = False
                        break
                else:
                    try:
                        if np.all(wordMatrix[idxi + idxl][idxj + idxl] != "" and wordMatrix[idxi + idxl][idxj + idxl] != letter):
                            possible = False
                    except IndexError:
                        possible = False
                        break
            if possible:
                checkList.add((idxi, idxj))
    return checkList

def randomDirection(wordMatrix, word):
    directions = {1, 2, 3}
    direction = random.sample(directions, 1)
    direction = direction[0]
    directions.remove(direction)
    checkList = wordCheck(direction, word, wordMatrix)
    while len(checkList) < 1:
        try:
            direction = random.sample(directions, 1)
            direction = direction[0]
            directions.remove(direction)
        except ValueError:
            return None, 0
        checkList = wordCheck(direction, word, wordMatrix)
    return direction, len(directions)

def insertWord(wordMatrix):  # I want to create a better system to utilize the checkMatrix, to ensure all words are in if possible
    word = getWord()
    while word is None:
        if len(tempWordBank) < 1:
            return wordMatrix
        word = getWord()
    direction, directions = randomDirection(wordMatrix, word)
    while direction is None:
        while directions < 1:
            word = getWord()
            while word is None:
                if len(tempWordBank) < 1:
                    return wordMatrix
            word = getWord()
        direction = randomDirection(wordMatrix, word)
        direction = randomDirection(wordMatrix, word)
    checkList = wordCheck(direction, word, wordMatrix)
    if direction == 1:    # Horizontal
        pos = random.sample(checkList, 1)
        x, y = pos[0]
        for letter in word:
            wordMatrix[x][y] = letter
            y += 1
    elif direction == 2:  # Vertical
        pos = random.sample(checkList, 1)
        x, y = pos[0]
        for letter in word:
            wordMatrix[x][y] = letter
            x += 1
    else:                 # Diagonal
        pos = random.sample(checkList, 1)
        x, y = pos[0]
        for letter in word:
            wordMatrix[x][y] = letter
            x += 1
            y += 1
    return wordMatrix



print(f"{wordBank}")
wordList = initMatrix(rows, cols)
while len(tempWordBank) > 0:
    wordList = insertWord(wordList)

wordList = randLetterMatrix(wordList)

printMatrix(wordList)

# print(wordCheck(1, wordBank[0], wordList))
