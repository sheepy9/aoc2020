import numpy

f = open("seats")
seats = f.read().split("\n")
while seats[-1] == "":
    seats.pop()

# part one
seats = ";".join(seats).replace("L","0 ").replace(".","0.1 ").replace("#","1 ")

seatMatrix = numpy.matrix(seats)
seatMatrix = numpy.pad(seatMatrix,1,mode='constant',constant_values=0.1)

rows, cols = numpy.shape(seatMatrix)

seatMatrixNew = numpy.array(seatMatrix, copy=True)
firstRun = True
while (not (numpy.array_equal(seatMatrix, seatMatrixNew))) or firstRun:
    seatMatrix = numpy.array(seatMatrixNew, copy=True)
    for m in range(1,rows-1):
        for n in range(1,cols-1):
            if seatMatrix[m][n] == 0.1:
                continue
            occupied = sum(sum(seatMatrix[m-1:m+2,n-1:n+2]))-seatMatrix[m][n]
            if seatMatrix[m][n] == 1 and occupied >= 4:
                seatMatrixNew[m][n] = 0
            if seatMatrix[m][n] == 0 and occupied < 1:
                seatMatrixNew[m][n] = 1
    firstRun = False

takenSeats = sum(seatMatrixNew[(seatMatrixNew==1)])
print(takenSeats)