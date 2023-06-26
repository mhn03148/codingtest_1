N = int(input())
stuNum = []
storage = []
answer = 0
for i in range(N):
    stuNum.append(input())

long = len(stuNum[0])
#print(long)

for i in range(1, long):
    for j in range(len(stuNum)):
        storage.append(stuNum[j][long-i:long])
    storageSet = set(storage)
    #print(storage, storageSet)
    #print(len(storage), len(storageSet))
    if len(storageSet) == N:
        answer = len(storage[0])
        break
    else:
        storage.clear()
        #storageSet.clear()

if answer == 0:
    answer = len(stuNum[0])
    print (answer)
else:
    print(answer)
