S = int(input())
ans = 0

while S > 0:
    if S>5 :
        ans = ans + S//5
        S = S % 5
    else:
        if S % 3 !=0:
            ans = -1
            break
        else:
            ans = ans + S//3
            S = S % 5
print(ans)