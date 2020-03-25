minutes_for_sleep = int(input())
hours = int(input())
minutes = int(input())
if minutes_for_sleep < 60:
    hours_for_sleep = 0
    minutes_for_sleep = minutes_for_sleep
else :
    hours_for_sleep = minutes_for_sleep // 60
    minutes_for_sleep = minutes_for_sleep % 60
#Высчитываем час и минуты , в котором надо встать
hours_wake_up = hours + hours_for_sleep
minutes_wake_up = minutes + minutes_for_sleep
if minutes_wake_up > 60:
    hours_wake_up += minutes_wake_up // 60
    minutes_wake_up = minutes_wake_up % 60
print(hours_wake_up)
print(minutes_wake_up)


