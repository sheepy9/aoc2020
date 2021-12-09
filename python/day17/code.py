import numpy

f = open("cube")
initCube = f.read().replace("#","1 ").replace(".","0 ").split("\n")
while initCube[-1] == "":
    initCube.pop()

# part one
initCube = ";".join(initCube)
initCube = numpy.pad(numpy.matrix(initCube),2,mode='constant')
matrix = numpy.zeros((numpy.shape(initCube)[0],numpy.shape(initCube)[1],5))
matrix[:,:,2] = initCube

for i in range(0,6):
    m,n,p = numpy.shape(matrix)
    newMatrix = numpy.ndarray.copy(matrix)
    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,p):
                ngbhrs = numpy.sum(matrix[i-1:i+2,j-1:j+2,k-1:k+2]) - matrix[i,j,k]
                if matrix[i,j,k] == 1:
                    if not (ngbhrs == 3 or ngbhrs == 2):
                        newMatrix[i,j,k] = 0
                elif matrix[i,j,k] == 0:
                    if ngbhrs == 3:
                        newMatrix[i,j,k] = 1

    matrix = numpy.ndarray.copy(newMatrix)
    padCheck = numpy.ndarray.copy(newMatrix)
    padCheck[2:-2,2:-2,2:-2] = 0
    if numpy.sum(padCheck) > 0:
        matrix = numpy.pad(matrix, 1, mode='constant')

print(numpy.sum(matrix))

# part two
matrix = numpy.zeros((numpy.shape(initCube)[0],numpy.shape(initCube)[1],5,5))
matrix[:,:,2,2] = initCube

for i in range(0,6):
    m,n,p,q = numpy.shape(matrix)
    newMatrix = numpy.ndarray.copy(matrix)
    for i in range(1,m):
        for j in range(1,n):
            for k in range(1,p):
                for l in range(1,q):
                    ngbhrs = numpy.sum(matrix[i-1:i+2,j-1:j+2,k-1:k+2,l-1:l+2]) - matrix[i,j,k,l]
                    if matrix[i,j,k,l] == 1:
                        if not (ngbhrs == 3 or ngbhrs == 2):
                            newMatrix[i,j,k,l] = 0
                    elif matrix[i,j,k,l] == 0:
                        if ngbhrs == 3:
                            newMatrix[i,j,k,l] = 1

    matrix = numpy.ndarray.copy(newMatrix)
    padCheck = numpy.ndarray.copy(newMatrix)
    padCheck[2:-2,2:-2,2:-2,2:-2] = 0
    if numpy.sum(padCheck) > 0:
        matrix = numpy.pad(matrix, 1, mode='constant')

print(numpy.sum(matrix))