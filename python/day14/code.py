def formatTo36BitString(num):
    return format(num,"36b").replace(" ","0")

def applyMask(memKey, mask):
    xPos = [x for x, v in enumerate(mask) if v == 'X']
    t = list(memKey)
    for x in xPos:
        t[x] = "X"
    return "".join(t)

f = open("instructions")
instructions = f.read().split("\n")
while instructions[-1] == "":
    instructions.pop()

# part one
mem = dict()
mask = ""
andMask = ""
orMask = ""

for instruction in instructions:
    opCode = instruction.split(" = ")
    if opCode[0] == "mask":
        mask = opCode[1]
        andMask = int(mask.replace("X","1"),2)
        orMask = int(mask.replace("X","0"),2)
    else:
        memKey = opCode[0].strip("mem[]")
        mem[memKey] = (int(opCode[1]) & andMask) | orMask

print(sum(mem.values()))

# part two
mem = dict()
mask = ""
orMask = ""
for instruction in instructions:
    opCode = instruction.split(" = ")
    if opCode[0] == "mask":
        mask = opCode[1]
        orMask = int(mask.replace("X","0"),2)
    else:
        memKey = formatTo36BitString(int(opCode[0].strip("mem[]")) | orMask)
        memKeyMasked = applyMask(memKey, mask).replace("X","{}")
        power = memKeyMasked.count("{}")
        for i in range(0,2**power):
            mem[memKeyMasked.format(*list(format(i,str(power)+"b").replace(" ","0")))] = int(opCode[1])

print(sum(mem.values()))