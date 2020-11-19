import pretty_errors
import random
import numpy as np

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

rows = 5
cols = 5

wordBank = [
    "AMUSEMENT", "TEA", "AUTUMN", "APPLES", "BLACK", "CANDY", "BATS", "TEST", "BOO", "CAT",
    "COSTUMES", "DRACULA", "EERIE", "EXCITEMENT", "FRANKENSTEIN", "FRIGHTEN",
    "GAMES", "GHOSTS", "GOBLIN", "HALLOWEEN", "HARVEST", "HAYRIDE", "MASK",
    "MONSTER", "MUMMY", "NIGHT", "OCTOBER", "ORANGE", "PARTY", "PRANK", "PUMPKINS",
    "SAFE", "SCARE", "SHADOWS", "SKELETON", "SPIDER", "SPOOKY", "TRICKORTREAT", "WITCH"
]
wordBank.sort(key=lambda s: len(s))

tempWordBank = []
for idxw, word in enumerate(wordBank):
    tempWordBank.append([word, {1, 2, 3}])



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
    return "."

def randLetterMatrix(wordMatrix):
    for idxi, i in enumerate(wordMatrix):
        for idxj, j in enumerate(i):
            if wordMatrix[idxi][idxj] == "":
                wordMatrix[idxi][idxj] = getRandomLetter()
    return wordMatrix


def newWord():
    if len(tempWordBank) > 1:
        word = tempWordBank[-1][0]
    else:
        return None
    return word

def newDirection(word):
    if len(tempWordBank[-1][1]) < 1:
        tempWordBank.pop()
        return None
    direction = random.sample(tempWordBank[-1][1], 1)
    direction = direction[0]
    tempWordBank[-1][1].discard(direction)
    return direction

def wordCheck(word, direction, wordMatrix):
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
    if len(checkList) < 1:
        return None
    pos = random.sample(checkList, 1)
    pos = pos[0]
    return pos

def wordFinder(wordMatrix):
    word = newWord()
    if word is None:
        return None
    
    direction = newDirection(word)
    if direction is None:
        return wordFinder(wordMatrix)
    
    pos = wordCheck(word, direction, wordMatrix)
    if pos is None:
        try:
            wordBank.remove(word)
        except Exception:
            pass
        return wordFinder(wordMatrix)
    
    tempWordBank[-1][1].clear()
    info = [word, direction, pos]
    return info


def insertWord(word, direction, pos, wordMatrix):
    if direction == 1:    # Horizontal
        x, y = pos
        for letter in word:
            wordMatrix[x][y] = letter
            y += 1
    elif direction == 2:  # Vertical
        x, y = pos
        for letter in word:
            wordMatrix[x][y] = letter
            x += 1
    else:                 # Diagonal
        x, y = pos
        for letter in word:
            wordMatrix[x][y] = letter
            x += 1
            y += 1
    return wordMatrix



print(f"{wordBank}")
wordList = initMatrix(rows, cols)
while len(tempWordBank) > 0:
    info = wordFinder(wordList)
    if info is None:
        break
    insertWord(info[0], info[1], info[2], wordList)

wordList = randLetterMatrix(wordList)

printMatrix(wordList)
print(wordBank)