def verifyCombinataion(time, busses):
    #key_min = min(busses, key=busses.get)
    for busId in busses.keys():
        if (time+busses[busId])%busId != 0:
            return False
    return True

f = open("timetable")
timetable = f.read().split("\n")

myTime = timetable[0]
busses = timetable[1].replace(",x","").split(",")

# part one
nearestTime = dict()
for bus in busses:
    nearestTime[bus] = int(int(myTime)/int(bus))*int(bus)+int(bus)

key_min = min(nearestTime, key=nearestTime.get)
print((nearestTime[key_min]-int(myTime))*int(key_min))

# part two
busses = dict()
busList = timetable[1].split(",")
for index in range(0,len(busList)):
    if busList[index] == "x":
        continue
    busses[int(busList[index])] = index

maxId = max(busses.keys())

baseTime = 1
increment = 1
while True:
    myTime = baseTime
    busPairs = []
    for bus in busses:
        if baseTime%bus == 0:
            busPairs.append(bus)


    #print(myTime)
    if verifyCombinataion(myTime, busses):
        print("FOUND IT")
        break
    baseTime = baseTime + increment

print(myTime)