N = int(input())
phone = list(map(int,input().split()))
y = 0
m = 0
for i in range(len(phone)):
    if phone[i] % 29 == 0:
        y += (phone[i] // 30) * 10
    else:
        y += ((phone[i] // 30) + 1) * 10


for i in range(len(phone)):
    if phone[i] % 59  == 0:
        m += (phone[i] // 60) * 15
    else:
        m += ((phone[i] // 60) + 1) * 15



if y>m:
    print('M',m)
elif y == m:
    print("Y M", m)
else:
    print('Y', y)
