Number_of_programmers = int(input())
if Number_of_programmers % 10 == 0 or Number_of_programmers % 10 == 5 or Number_of_programmers % 10 == 6 or Number_of_programmers % 10 == 7 or Number_of_programmers % 10 == 8 or Number_of_programmers % 10 == 9:
    print(Number_of_programmers , 'программистов')
elif Number_of_programmers % 100 == 11 or Number_of_programmers % 100 == 12 or Number_of_programmers % 100 == 13 or Number_of_programmers % 100 == 14:
    print(Number_of_programmers, 'программистов')
elif Number_of_programmers % 10 == 1:
    print(Number_of_programmers, 'программист')
elif Number_of_programmers % 10 == 2 or Number_of_programmers % 10 == 3 or Number_of_programmers % 10 == 4 :
    print(Number_of_programmers, 'программиста')
