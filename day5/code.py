f = open("seats")

seats = f.read().split("\n")
seats.pop()

maxId = 0
rows = 127
seatIds = []

for seat in seats:
    seatRow = 0
    index = 7
    row = seat[:7]
    column = seat[7:]
    for c in row:
        if c == "B":
            seatRow = seatRow + 2**(index-1)
        index = index - 1

    seatColumn = 0
    index = 3
    for c in column:
        if c == "R":
            seatColumn = seatColumn + 2**(index-1)
        index = index - 1

    seatIds.append(seatRow*8 + seatColumn)
    maxId = max(maxId, seatRow*8 + seatColumn)

seatIds.sort()
for index in range(1, len(seatIds)-1):
    if seatIds[index]-seatIds[index-1] > 1:
        print(seatIds[index-1])
        print(seatIds[index])
        print(seatIds[index]-1)
print(maxId)
        