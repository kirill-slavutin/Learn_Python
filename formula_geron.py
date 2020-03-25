AB = int(input())
BC = int(input())
AC = int(input())
semi_perimeter = (AB+BC+AC) / 2
square = (semi_perimeter * (semi_perimeter - AB) * (semi_perimeter - BC) * (semi_perimeter - AC)) ** 0.5
print(square)