s = input()
b = 0
ans = 0
num = []
sign = []
sign.append("+")
for i in range(len(s)):
    if s[i] == "+" or s[i] == "-":
        sign.append(s[i])
        a = s[b:i]
        b = i+1
        num.append(int(a))
num.append(int(s[b:]))
for i in range(len(sign)):
    if sign[i] == '-'and i+1 != len(sign):
        sign[i+1] = '-'

for i in range(len(num)):
    if sign[i] == '+':
        ans = ans+num[i]
    else:
        ans = ans - num[i]
print(ans)