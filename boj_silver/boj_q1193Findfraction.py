num = int(input())
i = 1
ans = 1
while num > ans:
    i = i + 1
    ans = ans + i

ja = 0
for j in range (1,i):
    ja = ja + j

if i % 2 ==0:
    print("{}/{}".format(num-ja,(i+1)-(num-ja)))
else:
    print("{}/{}".format((i + 1) - (num - ja),num - ja))