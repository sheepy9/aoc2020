f = open("slope")
slope = f.read()

slope = slope.split("\n")
slope.pop()

mMax = len(slope)
nMax = len(slope[0])

#part one
print("Part one:")
n = 0
inc = 3
treeCnt = 0
for m in range(0,mMax):
    if(slope[m][n%nMax] == "#"):
        treeCnt = treeCnt + 1
    n = n + inc

print(treeCnt)

#part two
print("Part two:")
acc = 1;
# down 1, right 1,3,5,7
for inc in range(1,8,2):
    n = 0
    treeCnt = 0
    for m in range(0,mMax):
        if(slope[m][n%nMax] == "#"):
            treeCnt = treeCnt + 1
        n = n + inc
    print(treeCnt)
    acc = acc*treeCnt

n = 0
inc = 1
treeCnt = 0
# down 2, right 1
for m in range(0,mMax,2):
    if(slope[m][n%nMax] == "#"):
        treeCnt = treeCnt + 1
    n = n + inc

print(treeCnt)
acc = acc*treeCnt
print(acc)
