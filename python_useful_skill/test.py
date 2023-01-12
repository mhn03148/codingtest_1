str = input()

count = 0
ans=[]
for i in range(len(str)):
    if ord(str[i]) == i + 97:
        count+=1
    else:
        #print(count)
        break
print(count)
