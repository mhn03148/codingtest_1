c = ['black', 'brown', 'red', 'orange', 'yellow', 'green', 'blue', 'violet', 'grey', 'white']
ans=''
for i in range(2):
    ans = ans + str(c.index(input()))
print(int(ans) * (10**c.index(input())))
