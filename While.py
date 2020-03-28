# Task 1
# Sum = 0
# Number_1 = 1
#
# while Number_1 != 0:
#     Number_1 = int(input())
#     Sum += Number_1
# print(Sum)
#
NOK = 0
input1 = int(input())
input2 = int(input())
if input1 > input2:
    NOK = input1
else:
    NOK = input2
while True:
    if((NOK % input1 == 0) and (NOK % input2 == 0)):
        break
    NOK += 1
print(NOK)

