x = int(input())
ans = 0
while x >0:
    if x == 64:
        x = x-64
        ans += 1
    elif 64 > x and 32 <= x:
        x = x -32
        ans += 1
    elif 32 > x and 16 <= x:
        x = x -16
        ans += 1
    elif 16 > x and 8 <= x:
        x = x -8
        ans += 1
    elif 8 > x and 4 <= x:
        x = x -4
        ans += 1
    elif 4 > x and 2 <= x:
        x = x -2
        ans += 1
    elif 2 > x and 1 <= x:
        x = x -1
        ans += 1
print(ans)