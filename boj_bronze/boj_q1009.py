T = int(input())
ans = []
for i in range(T):
    a, b = map(int, input().split())
    if a % 10 == 0:
        ans.append(10)
    elif a % 10 == 1:
        ans.append(1)
    elif a % 10 == 5:
        ans.append(5)
    elif a % 10 == 6:
        ans.append(6)
    elif a % 10 == 9:
        if b % 2 == 1:
            ans.append(9)
        else:
            ans.append(1)
    elif a % 10 == 4:
        if b % 2 == 1:
            ans.append(4)
        else:
            ans.append(6)
    else:
        ans.append(((a%10) ** (b%4))%10)
        print(i)
for i in ans:
    print(i, end = "\n")