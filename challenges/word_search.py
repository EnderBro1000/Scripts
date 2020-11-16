import pretty_errors
import random
import numpy as np

rows = 8
cols = 9

wordBank = [
    "AMUSEMENT"#, "AUTUMN", "APPLES", "BLACK", "CANDY", "BATS", "TEST", "BOO", "CAT"#,
    # "COSTUMES", "DRACULA",	"EERIE"," EXCITEMENT", "FRANKENSTEIN", "FRIGHTEN",
    # "GAMES", "GHOSTS", "GOBLIN", "HALLOWEEN", "HARVEST", "HAYRIDE", "MASK",
    # "MONSTER", "MUMMY", "NIGHT", "OCTOBER", "ORANGE", "PARTY", "PRANK", "PUMPKINS",
    # "SAFE", "SCARE", "SHADOWS", "SKELETON", "SPIDER", "SPOOKY", "TRICKORTREAT", "WITCH"
]
tempWordBank = wordBank

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def checkAppend(list, addition):
    for i in list:
        if i == addition:
            return list
    return list.append(addition)

def getRandomLetter():
    # return letters[random.randint(0, len(letters) - 1)]
    return "0"

def getWord():
    try:
        word = tempWordBank.pop(0)
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
    possible = False
    # printMatrix(wordMatrix)
    checkMatrix = np.ones((rows, cols), dtype=int)
    for idxi, i in enumerate(checkMatrix):
        for idxj, j in enumerate(i):
            for idxl, letter in enumerate(word):
                if direction == 1:
                    try:
                        # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi][idxj + idxl] == "" or wordMatrix[idxi][idxj + idxl] == letter:
                            possible = True
                        else:
                            checkMatrix[idxi][idxj] = 0
                    except IndexError:
                        checkMatrix[idxi][idxj] = 0
                if direction == 2:
                    try:
                    # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi + idxl][idxj] == "" or wordMatrix[idxi + idxl][idxj] == letter:
                            possible = True
                        else:
                            checkMatrix[idxi][idxj] = 0
                    except IndexError:
                        checkMatrix[idxi][idxj] = 0
                else:
                    try:
                        # print(wordMatrix[idxi][idxj + idxl] + "==" + letter)
                        if wordMatrix[idxi + idxl][idxj + idxl] == "" or wordMatrix[idxi + idxl][idxj + idxl] == letter:
                            possible = True
                        else:
                            checkMatrix[idxi][idxj] = 0
                    except IndexError:
                        checkMatrix[idxi][idxj] = 0
    return checkMatrix, possible

def wordCheck2(direction, word, wordMatrix):
    pos = set()
    for idxi, i in enumerate(wordMatrix):
        for idxj, j in enumerate(i):
            for idxl, letter in enumerate(word):
                if direction == 1:
                    try:
                        if np.all(wordMatrix[idxi][idxj + idxl] != "" and wordMatrix[idxi][idxj + idxl] != letter):
                            pos.add((idxi, idxj))
                    except IndexError:
                        pos.add((idxi, idxj))
                elif direction == 2:
                    try:
                        if np.all(wordMatrix[idxi + idxl][idxj] != "" and wordMatrix[idxi + idxl][idxj] != letter):
                            pos.add((idxi, idxj))
                    except IndexError:
                        pos.add((idxi, idxj))
                else:
                    try:
                        if np.all(wordMatrix[idxi + idxl][idxj + idxl] != "" and wordMatrix[idxi + idxl][idxj + idxl] != letter):
                            pos.add((idxi, idxj))
                    except IndexError:
                        pos.add((idxi, idxj))
    return pos

def insertWord(wordMatrix):  # I want to create a better system to utilize the checkMatrix, to ensure all words are in if possible
    word = getWord()
    if word is None:
        return wordMatrix
    directions = list(range(1, 4))
    random.shuffle(directions)
    # print(directions)  # horizontal: 1, vertical: 2, diagonal: 3
    try:
        direction = directions.pop()
    except IndexError:
        return wordMatrix
    checkList = wordCheck2(direction, wordMatrix, word)
    for direction in directions:
        while len(checkList) == 0:
            try:
                direction = directions.pop()
            except IndexError:
                word = getWord()
                if word is None:
                    return wordMatrix
            checkList = wordCheck2(direction, wordMatrix, word)
    print(f"direction: {direction}")
    if direction == 1:    # Horizontal
        print(f"{checkList} this is insertword")
        pos = random.sample(checkList, 1)
        x, y = pos[0]
        print(x, y)
        for letter in word:
            wordMatrix[x][y] = letter
            x += 1
    elif direction == 2:  # Vertical
        print(f"{checkList} this is insertword")
        pos = random.sample(checkList, 1)
        x, y = pos[0]
        print(x, y)
        for letter in word:
            wordMatrix[x][y] = letter
            y += 1
    else:                 # Diagonal
        print(f"{checkList} this is insertword")
        pos = random.sample(checkList, 1)
        x, y = pos[0]
        print(x, y)
        for letter in word:
            wordMatrix[x][y] = letter
            x += 1
            y += 1
    return wordMatrix



print(f"{wordBank}")
wordList = initMatrix(rows, cols)
while len(tempWordBank) > 0:
    wordList = insertWord(wordList)

print(wordList)
wordList = randLetterMatrix(wordList)

printMatrix(wordList)

# There seems to be an infinite loop somewhere, need to find it later
