f = open("instructions")
instructions = f.read().split("\n")
instructions.pop()

def switchInstruction(inst):
    if inst[0:3]=="nop":
        return "jmp"+inst[3:]
    elif inst[0:3]=="jmp":
        return "nop"+inst[3:]
    else:
        return "INVALID INSTRUCTION"
    
# part one
index = 0
acc = 0
indexList = []
while index not in indexList:
    indexList.append(index)
    instruction = instructions[index]
    opcode = instruction.split(" ")[0]
    opval = instruction.split(" ")[1]

    if opcode == "acc":
        acc = acc+int(opval)
    elif opcode == "jmp":
        index = index + int(opval)
        continue
    elif opcode == "nop":
        pass
    else:
        print("INVALID OP CODE") 

    index = index + 1

print("acc = " + str(acc))

# part two
nopjmp = []
index = 0
for instruction in instructions:
    if (instruction.find("nop")) != -1 or (instruction.find("jmp")) != -1:
        nopjmp.append(index)
    index = index + 1


codeLength = len(instructions)
for indexSwitch in nopjmp:
    index = 0
    acc = 0
    indexList = []
    newInstructions = instructions[:]
    newInstructions[indexSwitch] = switchInstruction(newInstructions[indexSwitch])
    while index not in indexList:
        indexList.append(index)
        instruction = newInstructions[index]
        opcode = instruction.split(" ")[0]
        opval = instruction.split(" ")[1]

        if opcode == "acc":
            acc = acc+int(opval)
        elif opcode == "jmp":
            index = index + int(opval)
            if index > codeLength:
                print("jumping out of bounds")
                break
            if index == codeLength:
                print("jumping to completion for acc=" + str(acc))                
                break
            else:
                continue
        elif opcode == "nop":
            pass
        else:
            print("INVALID OP CODE") 

        index = index + 1
        if index >= codeLength:
            print("program reached completion for acc=" + str(acc))
            break

    