N = input()
Lord = list(map(str, input().split()))
x, y = 1,1

for i in Lord:
    if(i == 'U'):
        if(x==1):
            x=x
        else:
            x-=1
    elif(i == 'D'):
        if(x==N):
            continue
        else:
            x+=1
    elif (i == 'R'):
        if (y == N):
            continue
        else:
            y += 1
    elif (i == 'L'):
        if (y == 1):
            continue
        else:
            y -= 1

print(x, y)