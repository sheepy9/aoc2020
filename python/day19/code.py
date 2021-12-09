def resolveMsg(ruleDict, )

f = open("input2")
inputText = f.read()
rules = inputText.split("\n\n")[split("\n")
messages = inputText.split("\n\n")[1].split("\n")

while rules[-1] == "":
    rules.pop()

while messages[-1] == "":
    messages.pop()

ruleDict = dict()
for rule in rules:
    ruleNum = rule.split(":")[0]
    recipe = rule.split(":")[1]
    ruleDict[int(ruleNum)] = recipe.strip().replace("\"","").replace(" | ","|").split("|")