time = 0
for i in range(4):
    time += int(input())

h = time // 60
m = time % 60
print(h)
print(m)