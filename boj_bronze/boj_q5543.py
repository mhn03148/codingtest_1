burger = []
drink = []
for i in range(3):
    burger.append(int(input()))

for i in range(2):
    drink.append(int(input()))

print(min(burger) + min(drink) - 50)