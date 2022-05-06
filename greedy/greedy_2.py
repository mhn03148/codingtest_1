N, M = map(int,(input().split()))

max = 0
data = []
for i in range(N):
    data.append (list (map(int, input().split())))
    data[i].sort()
    if max < data[i][0]:
        max = data[i][0]

print(max)