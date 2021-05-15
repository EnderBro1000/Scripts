import io

def dayCount(date):
    monthLengths = {
        "1" : 0,
        "2" : 31,
        "3" : 59,
        "4" : 90,
        "5" : 120,
        "6" : 151,
        "7" : 181,
        "8" : 212,
        "9" : 243,
        "10" : 273,
        "11" : 304,
        "12" : 334
    }

    date = date.split("/")
    days = 0
    days += monthLengths[date[0]]
    days += int(date[1])
    days += int(date[2]) * 365
    return days

    

def importFile(filePath):
    return open(filePath, "r").read()

def importSplitFile(filePath):
    file = importFile(filePath)
    return file.splitlines()

def getSubstringAtIndex(string, splitChar, index):
    return string.split(splitChar)[index]

def substringsAtIndex(lines, splitChar, index):
    out = []
    for string in lines:
        out.append(getSubstringAtIndex(string, splitChar, index))
    return out

def countItemsInList(substrings):
    subSet = []
    [subSet.append(x) for x in substrings if x not in subSet]
    fileTypes = []
    for fileType in subSet:
        fileTypes.append([fileType, substrings.count(fileType)])
    return fileTypes

def dayDateDiff(dateFrom, dateTo):
    return dayCount(dateFrom) - dayCount(dateTo)

def getDaysFromDates(dateFrom, datesTo):
    dateDiffs = []
    for dateTo in datesTo:
        dateDiffs.append(dayDateDiff(dateFrom, dateTo))
    return dateDiffs

def englishLists(pairs):
    out = ""

    for pair in pairs:
        for j, item in enumerate(pair):
            out += str(pair[j])
            if j < len(pair)-1:
                out += ", "
        out += "\n"

    return out

def concatenateLists(list1, list2):
    concatList = []
    for i in range(min(len(list1), len(list2))):
        concatList.append([list1[i], list2[i]])
    return concatList


def concatenateListsIndefinite(*matrix):
    concatList = []
    # for i in range(min([len(listicle) for listicle in matrix])): # returns the min of the length of all the lists in matrix (iterates i to that) (all it does is limit concatList range to the smallest list)
    for i in range(len(matrix[0])):
        items = []
        for listicle in matrix: # listicle is each list in matrix
            try:
                items.append(listicle[i])
            except IndexError:
                items.append(None)
        concatList.append(items)
    return concatList
    

def softwareListCheck(softwareListDays):
    oldList = []
    for software in softwareListDays:
        oldList.append(isSoftwareOld(software))
    return oldList

def isSoftwareOld(dayCount): # is an individual date from software considered old
    return dayCount > 180

def main():
    print("\tChallenge 3:")
    ch3 = countItemsInList(substringsAtIndex(importSplitFile("Prob03.in.txt"), ".", -1))
    print(englishLists(ch3))

    
    print("\tChallenge 5:")
    dates = substringsAtIndex(importSplitFile("Prob05.in.txt"), ":", -1)
    compareDate = dates[0]
    days = getDaysFromDates(compareDate, dates[1:])
    softwareOldList = softwareListCheck(days)
    softwareNames = substringsAtIndex(importSplitFile("Prob05.in.txt"), ":", 0)[1:]


    # print("Print expected:")
    # ch5 = concatenateLists(softwareNames, softwareOldList)
    # print(englishLists(ch5))

    print("Print listicle of lists' lists of lists:")
    listicle = concatenateListsIndefinite(softwareNames, softwareOldList, days)
    #print(listicle)
    print(englishLists(listicle))
    

main()
