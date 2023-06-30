roomNumber = input()
setDict = {}
setting = 0
for i in range(10):
    setDict[i] = 0

for i in range(len(roomNumber)):
    if int(roomNumber[i]) != 6 and int(roomNumber[i]) != 9 :
        if setDict[int(roomNumber[i])] == 0:
            for j in range(10):
                setDict[j] += 1
            setting += 1
            setDict[int(roomNumber[i])] -= 1
        else:
            setDict[int(roomNumber[i])] -= 1
    elif int(roomNumber[i]) == 6 :
        if setDict[int(roomNumber[i])] == 0 and setDict[9] == 0:
            for j in range(10):
                setDict[j] += 1
            setting += 1
            setDict[int(roomNumber[i])] -= 1
        elif setDict[int(roomNumber[i])] == 0 and setDict[9] != 0:
            setDict[9] -= 1
        else:
            setDict[6] -= 1

    elif int(roomNumber[i]) == 9:
        if setDict[int(roomNumber[i])] == 0 and setDict[6] == 0:
            for j in range(10):
                setDict[j] += 1
            setting += 1
            setDict[int(roomNumber[i])] -= 1
        elif setDict[int(roomNumber[i])] == 0 and setDict[6] != 0:
            setDict[6] -= 1
        else:
            setDict[9] -= 1

print(setting)