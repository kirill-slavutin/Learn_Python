number_1 = float(input())
number_2 = float(input())
operation = input()
if operation == '+':
    print(number_1 + number_2)
elif operation == '-':
    print(number_1 - number_2)
elif operation == '/':
    if number_2 == 0:
        print("Деление на 0!")
    else:
        print(number_1 / number_2)
elif operation == '*':
    print(number_1 * number_2)
elif operation == 'mod':
    if number_2 == 0:
        print("Деление на 0!")
    else:
        print(number_1 % number_2)
elif operation == 'pow':
    print(number_1 ** number_2)
elif operation == 'div':
    if number_2 == 0:
        print("Деление на 0!")
    else:
        print(number_1 // number_2)