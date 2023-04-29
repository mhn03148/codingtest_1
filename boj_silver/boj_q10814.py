T = int(input())
name_list = []

for i in range(T):
    a,b = (map(str, input().split()))
    name_list.append((int(a),b))

name_list.sort(key=lambda x : x[0])

for i in range(len(name_list)):
    print(name_list[i][0], name_list[i][1])