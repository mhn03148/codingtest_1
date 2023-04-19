c = int(input())
word = []
ans = []
for i in range(c):
    word.append(input())

#배열에서 중복된 단어가 있을시 set 기억할것
word_list = set(word)
word = list(word_list)
word.sort()
word.sort(key=len)



for i in range((len(word))):
    print(word[i], end='\n')
