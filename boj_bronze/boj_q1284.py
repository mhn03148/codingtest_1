number = ""

while number != "0":
    number = input()
    if number == "0":
        break

    answer = len(number) + 1
    for i in number:
        if i == "1":
            answer += 2
        elif i == "0":
            answer += 4
        else:
            answer += 3
    print(answer)