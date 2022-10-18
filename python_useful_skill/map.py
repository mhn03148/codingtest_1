#map(적용할 함수, 순회 가능한 객체)
a = list(map(int,['1','2',2.5])) # [1, 2, 2]
print(a)

#map 함수 인덱싱
ten_times = map(lambda x : 10 * x, (1,2,3,4,5))
#인덱싱 불가
print(list(ten_times)[0]) #10

