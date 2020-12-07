import re
import time 

global luggage

def resolve(bagArg):
    retVal = ""
    match = re.search("[0-9]+ ", bagArg)

    if type(match) == type(None):
        print("reached end node " + bagArg)
        return "(1)"
    print(match)
    
    bag = bagArg[match.end():]
    mul = int(bagArg[match.start():match.end()])
    print(bag)
    print(mul)
    for bags in luggage:
        bagList = bags.split(" contain ")
        if(bag == bagList[0]):
            targetBags = bagList[1].replace(".","").split(", ")
            print(targetBags)
            for target in targetBags:
                retVal = retVal + "(" + str(mul) + "*" + resolve(target) + ")"
            return retVal

        



start_time = time.time()
f = open("luggage")
luggage = f.read()
luggage = luggage.replace(" bags","")
luggage = luggage.replace(" bag","")
luggage = luggage.split("\n")
luggage.pop()

targets = {"shiny gold": 1}

while True:
    startLength = len(targets)
    for bags in luggage:
        bagList = bags.split(" contain ")

        newTargets = {}
        for key in targets.keys():
            match = re.search("[0-9]+ " + key, bagList[1])
            if type(match) != type(None):
                matchedBag = bagList[1][match.start():match.end()]
                matchedNum = re.search("[0-9]+", matchedBag)

                multiplyer = int(matchedBag[matchedNum.start():matchedNum.end()])
                matchedBag = matchedBag[int(matchedNum.end())+1:]
                if bagList[0] not in targets.keys():
                    newTargets[bagList[0]] = targets[key]*multiplyer
                    #print("every " + bagList[0] + " bag contains " + str(multiplyer) + " " + matchedBag +" bags, which is " + str(multiplyer*targets[key]) + " shiny gold bags")

        if newTargets != dict():
            targets.update(newTargets)

    if startLength == len(targets):
        break

colorSet = set(list(targets.keys()))
print(len(colorSet))

print(time.time()-start_time)

targets = {"shiny gold": 1}


# part two
secondSum = 0
while True:
    popList = []
    index = 0
    startLength = len(targets)
    for bags in luggage:
        tmp = 0
        bagList = bags.split(" contain ")

        newTargets = {}
        if bagList[0] in targets.keys():
            newTargetList = bagList[1].replace(".","").split(", ")
            for newTarget in newTargetList:
                match = re.search("^[0-9]+ ", newTarget)
                if type(match) != type(None):
                    matchedNum = int(newTarget[match.start():match.end()])
                    matchedBag = newTarget[match.end():]

                if matchedBag not in targets.keys():
                    newTargets[matchedBag] = targets[bagList[0]]*matchedNum
                    print("every " + bagList[0] + " bag contains " + str(matchedNum) + " " + matchedBag +" bags, which is " + str(matchedNum*targets[bagList[0]]) + " ")
                    print("adding " + str(matchedNum) + " to tmp sum")
                    tmp = tmp + matchedNum

        if newTargets != dict():
            targets.update(newTargets)
            popList.append(index)
            secondSum = secondSum + tmp

        index = index + 1

    if startLength == len(targets):
        break
