import average_speed

user_distance = float(input("Distance km: "))
user_time = float(input("Time hours: "))

print(f"Your average speed was {average_speed.calculate_average_speed(user_distance, user_time):.2f} km/h")