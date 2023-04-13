S = int(input())
ans = 0

while S >= 0:
    if S % 5 == 0 :
        ans = ans + S//5
        print(ans)
        break
    else:
        S = S -3
        ans = ans + 1
else:
    print(-1)

