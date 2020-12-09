def isSum(array):
    for x in array:
        index = 1
        for y in array[index:]:
            if numList[i] == x + y:
                return True
        index = index + 1
    return False

f = open("xmas")
numList = f.read().split("\n")
for i in range(0,numList.count("")):
    numList.remove("")
numList = [int(x) for x in numList]

# part one
sumLen = 25
for i in range(sumLen, len(numList)):
    found = isSum(numList[i-sumLen:i])
    if not found:
        magicNumber = numList[i]

print("no sum for " + str(magicNumber))

# part two
contiguousNums = []

for n in numList:
    if n == magicNumber:
        continue
    contiguousNums.append(n)
    while sum(contiguousNums) > magicNumber:
        contiguousNums.pop(0)
    if sum(contiguousNums) == magicNumber:
        break

print("sum is: " + str(min(contiguousNums) + max(contiguousNums)))
