num = input()
seat = input()

ans = seat.count("S") + (seat.count("L")//2)
if seat.count("L") == 0:
    print(ans)
else:
    print(ans+1)



