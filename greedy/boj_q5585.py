def greedy(C):
    a = 0
    while C > 0:
        if C >= 500:
            a = a+(C // 500)
            C = C % 500
        elif C < 500 and C >= 100:
            a = a+(C // 100)
            C = C % 100
        elif C < 100 and C >= 50:
            a = a+(C // 50)
            C = C % 50
        elif C < 50 and C >= 10:
            a = a+(C // 10)
            C = C % 10
        elif C < 10 and C >= 5:
            a = a+(C // 5)
            C = C % 5
        else:
            a = a + (C // 1)
            C = C % 1
    return a
mon = int(input())
print(greedy(1000-mon))