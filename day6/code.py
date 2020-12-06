from functools import reduce

f = open("answers")
groups = f.read().split("\n\n")

# part one
total = 0
for group in groups:
    answers = group.replace("\n","")
    total = total + len(set(answers))
print(total)

# part two
total = 0
for group in groups:
    answers = group.split("\n")
    answerSet = [set(ans) for ans in answers]
    total = total + len(reduce(lambda x, y: x & y, answerSet))
print(total)