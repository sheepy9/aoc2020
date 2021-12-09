def checkColumn(column, ruleList):
    validRules = []
    for index in range(0,len(ruleList)):
        ruleValid = True
        for val in column:
            if not inBounds(val, ruleList[index]):
                ruleValid = False
                break
        if ruleValid:
            validRules.append(index)
    return validRules

def inBounds(val, toupleList):
    retVal = False
    for bounds in toupleList:
        if val >= bounds[0] and val <=bounds[1]:
            retVal = True
    return retVal

def applyRules(val, ruleList):
    for rule in ruleList:
        if inBounds(val, rule):
            return True
    return False 

f = open("tickets")

# initial parsing 
ticketFile = f.read()
nearbyTickets = ticketFile.split("nearby tickets:\n")[1].split("\n")
myTicket = ticketFile.split("nearby tickets:\n")[0].split("your ticket:\n")[1]
myTicket = myTicket.replace("\n","").split(",")
ticketRules = ticketFile.split("your ticket:\n")[0]
ticketRules = ticketRules.split("\n")

while ticketRules[-1] == "":
    ticketRules.pop()

while myTicket[-1] == "":
    myTicket.pop()

while nearbyTickets[-1] == "":
    nearbyTickets.pop()

# creating ruleDict
ruleDict = dict()
for ticketRule in ticketRules:
    rule = ticketRule.split(": ")
    ranges = rule[1].split(" or ")
    ruleList = []
    for rang in ranges:
        bounds = rang.split("-")
        ruleList.append((int(bounds[0]),int(bounds[1])))
    ruleDict[rule[0]] = ruleList

# Relying on dictionary keys actually being ordered (only on python 3.6+)
validTickets = []
errorRate = 0
for ticket in nearbyTickets:
    validTickets.append(ticket)
    values = ticket.split(",")
    ruleList = list(ruleDict.values())
    index = 0
    for val in values:
        if not applyRules(int(val), ruleList):
            errorRate = errorRate + int(val)
            validTickets.pop()
            break
    
print(errorRate)

columns = []
for i in range(0,len(ruleList)):
    columns.append([])
    for ticket in validTickets:
        columns[i].append(int(ticket.split(",")[i]))

columnPossibilities = []
for column in columns:
    columnPossibilities.append(checkColumn(column, ruleList))

placedColumns = dict()
while len(placedColumns) < len(ruleList):
    index = 0
    for possibility in columnPossibilities:
        if len(possibility) == 1:
            placedColumns[index] = possibility[0]
        for colNum in possibility:
            if colNum in placedColumns.values():
                possibility.remove(colNum)
        index = index+1

mul = 1
for index in range(0,len(placedColumns)):
    if placedColumns[index] in range(0,6):
        mul = mul * int(myTicket[index])

print(mul)