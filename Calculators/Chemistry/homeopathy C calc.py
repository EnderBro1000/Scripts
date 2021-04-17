import numpy as np

def MCalc(startM):
    M = np.divide(startM, 100)
    return M

def cCalc(M, C, Ccount = 0):
    while Ccount < C:
        M = MCalc(M)
        Ccount += 1
    return M

F = cCalc(0.1, 161)
F = F * 6.02e23
print(F)