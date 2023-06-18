n = int(input())
password = []
for i in range(n):
    password.append(input())

for i in range(len(password)):
    if len(password[i]) >= 6 and len(password[i]) < 10 :
        password[i] = "yes"
    else:
        password[i] = "no"

for i in password:
    print(i,end="\n")

