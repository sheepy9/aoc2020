from functools import reduce

f = open("answers")
groups = f.read().split("\n\n")

# part one
total = sum([len(set(group.replace("\n",""))) for group in groups])
print(total)

# part two
total = 0
for group in groups:
    answers = group.split("\n")
    answerSet = [set(ans) for ans in answers]
    total = total + len(reduce(lambda x, y: x & y, answerSet))
print(total)
