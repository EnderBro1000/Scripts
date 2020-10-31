#variables: runs first
sides = [0, 0, 0]

print(int("10101", base=2))

useOriginalBase = int((input("What base would you like to use to enter in base?(input integer in base 10): ")))
useBase = int(input(f"What base would you like to use?(input integer in base {useOriginalBase}): "), base=useOriginalBase)

def based_float(i):
    i = int(i, base=useBase)
    return i

        
sidePos = 0
for side in sides:
    sides[sidePos] = based_float(input(f"side {sidePos + 1}: "))
    sidePos += 1



def right(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return False
    elif a ** 2 + b ** 2 == c ** 2:
        return True
    elif b ** 2 + c ** 2 == a ** 2:
        return True
    elif c ** 2 + a ** 2 == b ** 2:
        return True
    else:
        return False


print(f"Result: {right(sides[0], sides[1], sides[2])}")