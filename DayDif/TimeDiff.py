import datetime

# Prompt the user to enter the first time in HH:MM:SS format
first_time_str = input("Enter the Break In time (HH:MM:SS): ")
first_time = datetime.datetime.strptime(first_time_str, "%H:%M:%S")

# Prompt the user to enter the second time in HH:MM:SS format
second_time_str = input("Enter the Break Out time (HH:MM:SS): ")
second_time = datetime.datetime.strptime(second_time_str, "%H:%M:%S")

# Calculate the difference between the two times
time_diff = second_time - first_time

# Print the difference in HH:MM:SS format
print("Your total Break time is:", time_diff)

