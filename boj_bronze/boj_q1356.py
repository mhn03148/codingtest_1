N = list(map(int,input()))

if len(N) == 1:
    print("NO")
else:
    for i in range(len(N)-1):
        a = 1
        b = 1
        for j in range(i+1):
            a *= N[j]
        for k in range(i+1,len(N)):
            b *= N[k]
        if a == b:
            break

    if a == b:
        print("YES")
    else:
        print("NO")