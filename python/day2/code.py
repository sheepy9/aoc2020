# part one
f = open("passwords")
passwords = f.read().split("\n")
passwords.pop()
total = len(passwords)
valid = 0

for line in passwords:
    lineList = line.split(" ")
    rep = lineList[0]
    char = lineList[1][:-1]
    passw = lineList[2]
    cnt = passw.count(char)
    lower = int(rep.split("-")[0])
    upper = int(rep.split("-")[1])
    if(cnt <= upper and cnt >= lower):
        valid = valid+1
        
print(valid)

# part two
valid = 0
for line in passwords:
    lineList = line.split(" ")
    rep = lineList[0]
    char = lineList[1][:-1]
    passw = lineList[2]
    lower = int(rep.split("-")[0])
    upper = int(rep.split("-")[1])
    first = passw[lower-1]==char
    second = passw[upper-1]==char
    if(first != second):
        valid = valid+1

print(valid)
