global circularCompas

def moveToWaypoint(wayPoint, mul, distance):
    for key in distance.keys():
        distance[key] = distance[key] + mul*wayPoint[key]
    return distance

def rotateWaypoint(wayPoint, angleIndex):
    while abs(angleIndex) != 0:
        if angleIndex > 0:
            t = wayPoint["N"]
            wayPoint["N"] = wayPoint["E"]
            wayPoint["E"] = wayPoint["S"]
            wayPoint["S"] = wayPoint["W"]
            wayPoint["W"] = t
            angleIndex = angleIndex - 1
        else:
            t = wayPoint["N"]
            wayPoint["N"] = wayPoint["W"]
            wayPoint["W"] = wayPoint["S"]
            wayPoint["S"] = wayPoint["E"]
            wayPoint["E"] = t
            angleIndex = angleIndex + 1
    return wayPoint

f = open("directions")
directions = f.read().split("\n")
while directions[-1] == "":
    directions.pop()

# part one
compasDir = 3
circularCompas = ["N","W","S","E"]
distance = {"N":0, "S":0, "E":0, "W":0}

for direction in directions:
    if direction[0] in distance.keys():
        distance[direction[0]] = distance[direction[0]] + int(direction[1:])
    elif direction[0] == "F":
        distance[circularCompas[compasDir]] = \
                distance[circularCompas[compasDir]] + int(direction[1:])
    else:
        angleIndex = direction.replace("L","+")
        angleIndex = angleIndex.replace("R","-")
        angleIndex = int(int(angleIndex)/90)
        compasDir = (compasDir + angleIndex) % 4

print(abs(distance["N"] - distance["S"]) + abs(distance["E"]-distance["W"]))

# part two
distance = {"N":0, "S":0, "E":0, "W":0}
wayPoint = {"N":1, "S":0, "E":10, "W":0}
for direction in directions:
    if direction[0] in distance.keys():
        wayPoint[direction[0]] = wayPoint[direction[0]] + int(direction[1:])
    elif direction[0] == "F":
        distance = moveToWaypoint(wayPoint, int(direction[1:]), distance)
    else:
        angleIndex = direction.replace("L","+")
        angleIndex = angleIndex.replace("R","-")
        angleIndex = int(int(angleIndex)/90)
        wayPoint = rotateWaypoint(wayPoint, angleIndex)

print(abs(distance["N"] - distance["S"]) + abs(distance["E"]-distance["W"]))