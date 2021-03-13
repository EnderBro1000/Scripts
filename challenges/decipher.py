import numpy as np

sample_input = "GhduSocZrun"
sample_caesar = "GhduSocZrun"
sample_scytale ="aaaaaaaaaaaa"

apl = "abcdefghijklmnopqrstuvwxyz"
apu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def inRange(num, min, max):
    return num >= min and num <= max


def caesarShift(text, shift):
    decoded = ""
    decodedUni = ""
    for i, char in enumerate(text):
        # # unicode method
        # uniChar = ord(char)
        # shiftNow = uniChar + shift
        # if inRange(uniChar, 65, 90):
        #     # uppercase
        #     if shiftNow > 90:
        #         shiftNow -= 26
        # elif inRange(uniChar, 97, 122):
        #     # lowercase
        #     if shiftNow > 122:
        #         shiftNow -= 26
        # shiftChar = chr(shiftNow)
        # decodedUni += shiftChar

        # string method
        if apl.find(char) != -1:
            decoded += apl[apl.find(char) - shift]
        if apu.find(char) != -1:
            decoded += apu[apu.find(char) - shift]
    return decoded

def caesar(text):
    for x in range(26):
        caesarText = caesarShift(text, x)
        print(caesarText)
        temp = caesarText.lower()
        if temp.find("dear") != -1:
            return f" success: {caesarText}"
    return "not found"


def matrixSize(text):
    print(len(text))
    
    for rows in range(0, len(text) + 1):
        for cols in range(0, len(text) + 1):
            # print(f"attempt: {rows, cols}")
            if((rows * cols) == len(text)):
                print(f"success at pos: {rows, cols}")
    return rows, cols


def scytale(text):
    rows, cols = matrixSize(text)
    print(rows, cols)
    matrix = np.zeros(rows, cols)
    z = 0
    for i in range(cols):
        for j in range(rows):
            matrix[i][j] = text[z]
            z += 1
    
    print(matrix)
    return "DearPlzWork"
    #if stick == text.stick
        # return "dearPlzWork"
    

# print(caesar(sample_caesar))
scytale(sample_scytale)