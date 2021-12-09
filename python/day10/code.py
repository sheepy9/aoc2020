import numpy

f = open("adapters")
adapters = f.read().split("\n")
adapters.pop()
adapters = [int(x) for x in adapters]

# part one
adapters.insert(0,0)
adapters.sort()
npAdapters = numpy.array(adapters)
joltDiff = npAdapters[1:]-npAdapters[:-1]
joltDiff = numpy.append(joltDiff,[3])
unique, count = numpy.unique(joltDiff, return_counts=True)
uniqueCount = dict(zip(unique, count))
print(uniqueCount[1]*uniqueCount[3])

# part two
cnt = 0
mul = 1
luTable = [1,1,2,4,7,14]
for i in joltDiff:
    if(i == 1):
        cnt = cnt+1
    else:
        mul = mul * luTable[cnt]
        cnt = 0

print(mul)