recommendation_time = int(input())
max_time = int(input())
actual_time = int(input())
if recommendation_time <= actual_time <= max_time:
    print("Это нормально")
elif recommendation_time > actual_time:
    print("Недосып")
else:
    print("Пересып")


