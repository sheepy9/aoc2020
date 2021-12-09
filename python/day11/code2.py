import numpy

f = open("seats")
seats = f.read().split("\n")
while seats[-1] == "":
    seats.pop()

# part two
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
            # go in all 8 directions
            occupied = 0
            # go up
            for t in range(1,m):
                if seatMatrix[m-t,n] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m-t,n] == 0:
                    break
            # go up-right
            lim = min(cols-n-1, m)
            for t in range(1,lim):
                if seatMatrix[m-t,n+t] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m-t,n+t] == 0:
                    break
            # go right
            for t in range(1,cols-n):
                if seatMatrix[m,n+t] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m,n+t] == 0:
                    break
            # go down-right
            lim = min(cols-n-1, rows-m-1)
            for t in range(1,lim):
                if seatMatrix[m+t,n+t] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m+t,n+t] == 0:
                    break
            # go down
            for t in range(1,rows-m):
                if seatMatrix[m+t,n] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m+t,n] == 0:
                    break
            # go down-left
            lim = min(rows-m-1, n)
            for t in range(1,lim):
                if seatMatrix[m+t,n-t] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m+t,n-t] == 0:
                    break
            # go left
            for t in range(1,n):
                if seatMatrix[m,n-t] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m,n-t] == 0:
                    break
            # go up-left
            lim = min(m,n)
            for t in range(1,lim):
                if seatMatrix[m-t,n-t] == 1:
                    occupied = occupied + 1
                    break
                elif seatMatrix[m-t,n-t] == 0:
                    break
            
            if occupied >= 5:
                seatMatrixNew[m][n] = 0
            if seatMatrix[m][n] == 0 and occupied < 1:
                seatMatrixNew[m][n] = 1
    firstRun = False

takenSeats = sum(seatMatrixNew[(seatMatrixNew==1)])
print(takenSeats)