N, r, c = map(int,input().split())

print(N, r, c)


# for i in range(4):
#     for j in range(N):
#         print((0+i,0+i), (0+i,2**(N-j)), (2**(N-j),0+i), (2**(N-j),2**(N-j)))

for j in range(2**(N-1)):
    a = j * 2
    print((a, a))
    print((a, a+1))
    print((a+1, a))
    print((a+1, a+1))


#zfunc(N))
