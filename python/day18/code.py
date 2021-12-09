import re

# regex strings
NumPlusTimesNum = "[0-9]+[\+\*][0-9]+"
NumPlusNum = "[0-9]+[\+][0-9]+"
NumTimesNum = "[0-9]+[\*][0-9]+"

def evaluatePlusPrio(expr):
    expr = expr.replace("(","").replace(")","")
    retVal = expr
    # match num+num or num*num to enter loop
    match = re.search(NumPlusTimesNum, retVal)
    while type(match) != type(None):
        # evaluate all patterns num+num
        match = re.search(NumPlusNum, retVal)
        while type(match) != type(None):
            result = eval(match.group())
            exprList = list(retVal)
            del exprList[match.start():match.end()]
            exprList.insert(match.start(),str(result))
            retVal = "".join(exprList)
            match = re.search(NumPlusNum, retVal)

        # check for pattern num*num to do at least once
        match = re.search(NumTimesNum, retVal)
        while type(match) != type(None):
            result = eval(match.group())
            exprList = list(retVal)
            del exprList[match.start():match.end()]
            exprList.insert(match.start(),str(result))
            retVal = "".join(exprList)

            # check for pattern num+num
            match = re.search(NumPlusNum, retVal)
            if type(match) != type(None):
                print("breaking")
                break
            match = re.search(NumTimesNum, retVal)

        match = re.search(NumPlusNum, retVal)

    return retVal

def evaluate(expr):
    expr = expr.replace("(","").replace(")","")
    retVal = expr
    # match first num+num or num*num and evaluate
    match = re.search(NumPlusTimesNum, retVal)
    while type(match) != type(None):
        # evaluate matched expression
        result = eval(match.group())
        exprList = list(retVal)
        # replace expression with evaluated result
        del exprList[match.start():match.end()]
        exprList.insert(match.start(),str(result))
        retVal = "".join(exprList)
        # check for more num+num or num*num matches
        match = re.search(NumPlusTimesNum, retVal)

    return retVal

f = open("calculations")
calculations = f.read().replace(" ","").split("\n")

# part one
results = []
# go line by line through calculations
for line in calculations:
    # regex to match inner-most brackets
    match = re.search("\(([^\(\)]+)\)",line)
    while type(match) != type(None):
        # evaluate expression
        result = evaluate(match.group())
        lineList = list(line)
        # replace matched expression with evaluated result
        del lineList[match.start():match.end()]
        lineList.insert(match.start(), result)
        line = "".join(lineList)
        # check for more bracket matches
        match = re.search("\(([^\(\)]+)\)",line)
    # evaluate what is remaining from expression when all brackets are removed
    result = evaluate(line)
    results.append(int(result))

print(sum(results))

# part two
results = []
for line in calculations:
    match = re.search("\(([^\(\)]+)\)",line)
    while type(match) != type(None):
        result = evaluatePlusPrio(match.group())
        lineList = list(line)
        del lineList[match.start():match.end()]
        lineList.insert(match.start(), result)
        line = "".join(lineList)
        match = re.search("\(([^\(\)]+)\)",line)
    result = evaluatePlusPrio(line)
    results.append(int(result))

print(sum(results))