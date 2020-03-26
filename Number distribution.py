Number_1 = int(input())
Number_2 = int(input())
Number_3 = int(input())
if Number_1 > Number_2 and Number_1 > Number_3:
    print(Number_1)
    if Number_2 > Number_3:
        print(Number_3)
        print(Number_2)
    else:
        print(Number_2)
        print(Number_3)

if Number_2 > Number_1 and Number_2 > Number_3:
    print(Number_2)
    if Number_1 > Number_3:
        print(Number_3)
        print(Number_1)
    else:
        print(Number_1)
        print(Number_3)
if Number_3 > Number_1 and Number_3 > Number_2:
    print(Number_3)
    if Number_1 > Number_2:
        print(Number_2)
        print(Number_1)
    else:
        print(Number_1)
        print(Number_2)
if Number_1 == Number_2 == Number_3:
    print(Number_1)
    print(Number_1)
    print(Number_1)
if Number_1 == Number_2 and Number_1 > Number_3:
    print(Number_1)
    print(Number_3)
    print(Number_2)
if Number_1 == Number_3 and Number_1 > Number_2:
    print(Number_1)
    print(Number_2)
    print(Number_3)
if Number_2 == Number_3 and Number_2 > Number_1:
    print(Number_2)
    print(Number_1)
    print(Number_3)