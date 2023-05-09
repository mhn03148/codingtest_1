A, B, V = map(int, input().split())

count = (V-A) // (A-B)

if count*(A-B) < V-A:
    count+=1
print(count+1)