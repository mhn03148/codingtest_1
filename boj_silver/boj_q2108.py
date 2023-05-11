import math
N = int(input())
arr = []
di = {}
for _ in range(N):
    arr.append(int(input()))
arr.sort()

for i in arr:
    count = 0
    if  i in di:
        di[i] = di[i]+1
    else:
        di[i] = 1
print(round(sum(arr)/N))
print(arr[(N//2)])

#print(max(di.values()))
list = list(di.values())
list1 = di.keys()
ans=[]
list.sort(reverse=True)
if list.count(max(list))>1:
    for i in list1:
        if di[i] == max(list):
            ans.append(i)
    print(ans[1])
else:
    for i in list1:
        if di[i] == max(list):
            print(i)

print(max(arr)-min(arr))