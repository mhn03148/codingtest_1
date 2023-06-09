N = int(input())
soldierArray = list(map(int,input()))
soriderSave = []
for i in range(len(soldierArray)-1):
    count = 0
    soriderSave.append(soldierArray[i])
    for j in range(i+1,len(soldierArray)):
        if soriderSave[0] > soldierArray[j]:
