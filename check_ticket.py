Number = int(input())
balance = Number % 1000
x = balance % 10
y = balance // 100
z = balance % 100
h = z // 10
d = Number // 1000
i = d % 10
o = d // 100
p = d % 100
c = p // 10
if x + y + h == i + o + c:
    print('Счастливый')
else:
    print('Обычный')