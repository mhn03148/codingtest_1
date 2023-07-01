N, M = map(int, input().split(" "))
comArray = []
comHacMap = [0 for i in range(N)]
comDict = {}

for _ in range(M):
    firstNum, secondNum = map(int, input().split(" "))
    comArray.append([firstNum, secondNum])

for i in range(1,N+1):
    comDict[i] = []

for i in range(len(comArray)):
     comDict[comArray[i][0]].append(comArray[i][1])

print(comDict)
print(comArray)

for i in comDict:
    for j in comDict[i]:
        print(i, comDict[j])
    #print(comDict[i])


print(comHacMap)

