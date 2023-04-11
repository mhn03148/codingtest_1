def greedy(C):
    a, b, c, d = (0, 0, 0, 0)
    while C > 0:
        if C >= 25:
            a = C // 25
            C = C % 25
        elif C < 25 and C >= 10:
            b = C // 10
            C = C % 10
        elif C < 10 and C >= 5:
            c = C // 5
            C = C % 5
        else:
            d = C
            C = C % 1
    return a, b, c, d

T = int(input())
D=[]
for i in range(T):
    D.append(int(input()))
for i in range(len(D)):
    a1,b1,c1,d1 = greedy(D[i])
    print(a1,b1,c1,d1)




