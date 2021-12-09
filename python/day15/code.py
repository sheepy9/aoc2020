def findNthNumber(length):
    f = open("numbers")
    numbers = f.read().split("\n")[0].split(",")

    numDict = dict()

    spoken = []
    turn = 1
    for num in numbers:
        numDict[int(num)] = [0,turn]
        spoken.append(int(num))
        turn = turn + 1

    spoken.append(0)
    initLen = len(spoken)
    spoken = spoken[-2:]
    turn = turn+1
    for i in range(1,length-initLen+1):
        if spoken[-1] in numDict:
            numDict[spoken[-1]].append(turn-1)
            numDict[spoken[-1]].pop(0)
            spoken.append(turn-1-numDict[spoken[-1]][-2])
            spoken.pop(0)
            turn = turn + 1
        else:
            numDict[spoken[-1]] = [0,turn-1]
            spoken.append(0)
            spoken.pop(0)
            turn = turn + 1
    return(spoken[-1])

print(findNthNumber(2020))
print(findNthNumber(30000000))
