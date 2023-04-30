N = (input())

for i in range(int(N)):
    ans = 0
    num = str(i)
    for j in range(len(num)):
        ans = ans + int(num[j])
    ans +=i
    if int(N) == ans:
        print(i)
        break
if i == int(N)-1:
    print(0)
