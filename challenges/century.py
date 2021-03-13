year = input("Year: ")

def numInterpreter(num):
    if str(num):
        try:
            num = float(num)
            num = int(num)
            return num
        except:
            pass
    num = num.lower()
    num = num.replace("and ", "")
    num = num.replace(",", "")
    num = num.split(" ")
    wordToNum = {
        "" : 0,
        "one" : 1,
        "two" : 2,
        "three" : 3,
        "four" : 4,
        "five" : 5,
        "six" : 6,
        "seven" : 7,
        "eight" : 8,
        "nine" : 9,
        "twenty" : 20,
        "thirty" : 30,
        "fourty" : 40,
        "fifty" : 50,
        "sixty" : 60,
        "seventy" : 70,
        "eighty" : 80,
        "ninety" : 90,
        "hundred" : 100,
        "thousand" : 1000,
        "million" : 1000000
    }
    for pos, word in enumerate(num):
        try:
            num[pos] = int(word)
        except:
            try:
                num[pos] = wordToNum[word]
            except KeyError:
                raise ValueError("Word was unintelligible, check spelling and try again.")
    return num



def centuryFinder(year):
    try:
        year = float(year)
        year = int(year)
    except:
        raise ValueError("invalid input, must be a integer")
    year += 99
    year = year // 100
    return year

# print(centuryFinder())

print(numInterpreter(year))
