import re
import time 

global luggage

def resolve(bagArg):
    retVal = "0"
    match = re.search("[0-9]+ ", bagArg)

    if type(match) == type(None):
        return eval("0")
    
    bag = bagArg[match.end():]
    mul = int(bagArg[match.start():match.end()])
    for bags in luggage:
        bagList = bags.split(" contain ")
        if(bag == bagList[0]):
            targetBags = bagList[1].replace(".","").split(", ")
            for target in targetBags:                    
                retVal = retVal + "+" + "("+ str(resolve(target)) + ")"
            retVal = mul*eval(retVal) + mul
            return retVal


start_time = time.time()
f = open("luggage")
luggage = f.read()
luggage = luggage.replace(" bags","")
luggage = luggage.replace(" bag","")
luggage = luggage.split("\n")
luggage.pop()

# part one
targets = {"shiny gold"}

while True:
    startLength = len(targets)
    for bags in luggage:
        bagList = bags.split(" contain ")
        newTargets = set()
        for key in targets:
            match = re.search("[0-9]+ " + key, bagList[1])
            if type(match) != type(None):
                if bagList[0] not in targets:
                    newTargets.add(bagList[0])
        targets.update(newTargets)

    if startLength == len(targets):
        break

print("part one: " + str(len(targets)-1))


# part two
targets = "1 shiny gold"
print("part two: " + str(resolve(targets)-1))

print(time.time()-start_time)