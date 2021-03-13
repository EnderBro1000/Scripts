import numpy as np

sample_input = "JouyWOjkgrkgjIacuyzrgxgukoszoXxeejyreZyXJZokzrhngX"
sample_caesar = "GhduSocZrun"
sample_scytale ="hleols"


apl = "abcdefghijklmnopqrstuvwxyz"
apu = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def inRange(num, min, max):
    return num >= min and num <= max

def caesarShift(text, shift):
    decoded = ""
    for i, char in enumerate(text):
            # unicode method
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

def caesar(text, searchText):
    for x in range(26):
        caesarText = caesarShift(text, x)
        # print(caesarText)
        temp = caesarText.lower()
        if temp.find(searchText) != -1:
            return caesarText
    return False

def matrixSize(text):
    print(len(text))
    successes = []
    for rows in range(0, len(text) + 1):
        for cols in range(0, len(text) + 1):
            # print(f"attempt: {rows, cols}")
            if((rows * cols) == len(text)):
                successes.append([rows, cols])
                print(f"Matrix factor found: {rows, cols}")
    print(f"Matrix factor list: {successes}")
    return successes

def scytale(text, size):
    #z = 0 #position in the text 
    # out = ""
    out = ""
    for i in range(size[1]): #i and j are coords
        for j in range(size[0]):
            out += text[j * size[1] + i]
    return out
    
    #return False
    #if stick == text.stick
        # return "dearPlzWork"
    
def scytaleCaesar(text):
    possibleSizes = matrixSize(text)
    for size in possibleSizes:
        scytaleText = scytale(text, size)
        deciphered = caesar(scytaleText, "dear")
        if (deciphered != False):
            print(f"Decipher found! size: {size}") 
            return deciphered
    print("Decipher not found")
    return False
    
# print(caesar(sample_caesar))
# matrixSize(sample_scytale)
print(scytale(sample_input, [5,10]))
# print(scytaleCaesar(sample_input))
