def greedy(num):
    a,b,c = (0,0,0)
    while num > 0:
        if num >=300:
            a = num // 300
            num = num % 300
        elif num < 300 and num >=60:
            b = num // 60
            num = num % 60
        else:
            c = num // 10
            num = num % 10
            if num !=0:
                return -1
    return(a,b,c)
T = int(input())
if T % 10 == 0:
    d,e,f= greedy(T)
    print(d,e,f)
else:
    print(-1)