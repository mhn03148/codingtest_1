T = int(input())
i = 1
count=0
while T>i:
    i = i+6*count
    count+=1

if T ==1:
    print(1)
else:
    print(count)