in_minutes = int(input())
if in_minutes < 60:
    hours = 0
    minutes = in_minutes
else :
    hours = in_minutes // 60
    minutes = in_minutes % 60
print(hours)
print(minutes)