number_1 = float(input())
number_2 = float(input())
operation = input()
if number_2 == 0:
    print("Деление на 0!")
elif operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '/':
    print(number_1 / number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == 'mod':
    print(number_1 % number_2)
elif operation == 'pow':
    print(number_1 ** number_2)
elif operation == 'div':
    print(number_1 // number_2)