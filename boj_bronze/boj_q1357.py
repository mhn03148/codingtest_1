def Rec(x):
    y = ""
    for i in range(len(x)):
        y += x[len(x)-1 - i]
    return y

num1, num2 = map(str, input().split(" "))
num3 = str(int(Rec(num1)) + int(Rec(num2)))

print(int(Rec(num3)))
