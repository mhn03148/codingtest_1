T = int(input())
List = []
rank = []
for _ in range(T):
    List.append(list(map(int,input().split())))

for i in range(len(List)):
    count = 0
    for j in range(len(List)):
        if (List[i][1] < List[j][1] and List[i][0] < List[j][0]):
            count+=1
    rank.append(count+1)


for i in rank:
    print(i, end=" ")