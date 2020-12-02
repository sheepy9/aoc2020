f = open("expenses")
expenses = f.read().split("\n")
expenses.pop()

# Part one
index = 0
for n in expenses:
    for m in expenses[index:]:
        if(int(n)+int(m)==2020):
            print(int(m)*int(n))
            break
    index = index+1

# Part two
index = 0
for n in expenses:
    index2 = index
    for m in expenses[index:]:
        for p in expenses[index2:]:
            if(int(n)+int(m)+int(p)==2020):
                print(int(m)*int(n)*int(p))
                break
        index2 = index2+1
    index = index+1
