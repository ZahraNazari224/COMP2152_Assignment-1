"""
Author: Zahra Nazari
Assignment: #1
"""

# Step b: Create 4 variables
gym_member= "Alex Alliton"  #String
preferred_weight_kg = 20.5  #Float
highest_reps = 25           #int
membership_active = True    #bool

# Step c: Create a dictionary named workout_stats
workout_stats = {
    "Alex":(10,60, 40),
    "Jamie":(20, 50, 15),
    "Taylor": (30, 90, 30)
}

# Step d: Calculate total workout minutes using a loop and add to dictionary
workout_stats = {
    "Alex":(10,60, 40),
    "Jamie":(20, 50, 15),
    "Taylor": (30, 90, 30)
}
total = {}
for friend, amount in workout_stats.items():
    total[f"{friend}_Total"] = sum(amount)
   
workout_stats.update(total)

# Step e: Create a 2D nested list called workout_list
workout_stats = {
    "Alex":(10,60, 40),
    "Jamie":(20, 50, 15),
    "Taylor": (30, 90, 30)
}
workout_list = []
for friend, amount in workout_stats.items():
    workout_list.append(list(amount))



# Step f: Slice the workout_list
workout_stats = {
    "Alex":(10,60, 40),
    "Jamie":(20, 50, 15),
    "Taylor": (30, 90, 30)
}
workout_list = [list(minutes) for minutes in workout_stats.values()]
for friend in workout_list:
    print(friend[:2])
for friend in workout_list[-2:]:
    print(friend[2])

# Step g: Check if any friend's total >= 120
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (15, 10, 15),
    "Taylor": (60, 40, 90)
}

for friend, minutes in workout_stats.items():
    total_minutes = sum(minutes)

    if total_minutes >= 120:
        print(f"Great job staying active, {friend}!")

# Step h: User input to look up a friend
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (15, 10, 15),
    "Taylor": (35, 40, 30)
}

name = input("Enter a friend's name: ")

if name in workout_stats:
    yoga, running, weightlifting = workout_stats[name]
    total_minutes = sum(workout_stats[name])

    print(f"{name}'s workout minutes:")
    print(f"Yoga: {yoga}")
    print(f"Running: {running}")
    print(f"Weightlifting: {weightlifting}")
    print(f"Total minutes: {total_minutes}")
else:
    print(f"Friend {name} not found in the records.")

# Step i: Friend with highest and lowest total workout minutes
workout_stats = {
    "Alex": (30, 45, 20),
    "Jamie": (15, 10, 15),
    "Taylor": (35, 40, 30)
}

#dictionary for total minutes
total_minutes = {}

for friend, minutes in workout_stats.items():
    total_minutes[friend] = sum(minutes)

#highest and lowest amount
highest_friend = max(total_minutes, key=total_minutes.get)
lowest_friend = min(total_minutes, key=total_minutes.get)

print(f"Friend with highest total workout minutes: {highest_friend}")
print(f"Friend with lowest total workout minutes: {lowest_friend}")
