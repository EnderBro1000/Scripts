import random
import numpy as np

rows = 25
cols = 20

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

def randLetterMatrix(wordMatrix):
    # pos = 0
    for i in range(len(wordMatrix)):
        for j in range(len(wordMatrix[0])):
            wordMatrix[i][j] = getRandomLetter()
            # wordMatrix[i][j] = pos
            # pos += 1
    return wordMatrix




def insertWord(wordArray):
    word = getRandomWord()
    wordStart = 0
    direction = random.randint(1, 3)  # horizontal: 1, vertical: 2, diagonal: 3
    if direction == 1:    # Horizontal
        while len(word) > cols:
            word = getRandomWord()
        print(word)
        rowStart = random.randint(0, len(wordArray) - 1)
        colStart = random.randint(0, len(wordArray[rowStart]) - len(word))
        for letter in word:
            wordArray[rowStart][wordStart + colStart] = letter
            colStart += 1
    elif direction == 2:  # Vertical
        while len(word) > rows:
            word = getRandomWord()
        print(word)
        rowStart = random.randint(0, len(wordArray) - len(word))
        colStart = random.randint(0, len(wordArray[rowStart]) - 1)
        for letter in word:
            wordArray[wordStart + rowStart][colStart] = letter
            rowStart += 1
    else:                 # Diagonal
        while len(word) > rows or len(word) > cols:
            word = getRandomWord
        print(word)
        colStart = random.randint(0, len(wordArray) - len(word))
        rowStart = random.randint(0, len(wordArray[colStart]) - len(word))
        for letter in word:
            wordArray[wordStart + colStart][wordStart + rowStart] = letter
            rowStart += 1
            colStart += 1
    
    
# wordList = randLetterMatrix(initMatrix(rows, cols))
wordList = initMatrix(rows, cols)

insertWord(wordList)

printMatrix(wordList)
