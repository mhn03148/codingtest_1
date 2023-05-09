T = int(input())
ansArray = []
def ans(a,b):
    apart = [[1]*b for _ in range(a)]
    for i in range(a):
        if i == 0:
            for j in range(b):
                apart[i][j] = j+1
        else:
            for j in range(1,b):
                apart[i][j] = apart[i-1][j] + apart[i][j-1]
    return(apart[-1][-1])

for _ in range(T):
    a = int(input()) + 1
    b = int(input())
    ansArray.append(ans(a,b))

for i in ansArray:
    print(i, end="\n")