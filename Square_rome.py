type_figure = str(input())
pi = 3.14
if type_figure == 'круг':
    radius = int(input())
    print(pi * radius ** 2)
elif type_figure == 'прямоугольник':
    x = int(input())
    z = int(input())
    print(x*z)
elif type_figure == 'треугольник':
    a = int(input())
    b = int(input())
    c = int(input())
    semi_perimeter = (a + b + c) / 2
    print ((semi_perimeter * (semi_perimeter - a) * (semi_perimeter - b) * (semi_perimeter - c)) ** 0.5)