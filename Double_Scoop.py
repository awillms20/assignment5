# Task 1: Nested loops 
import random

moods= ['Happy','Sad','Energetic','Calm','Tierd']

week_days= ['Monday','Tuseday','Wednesday','Thursday','Friday']

time_of_day = ['Morning','Afternoon','Night']
for day in range(len(week_days)):
    for time in range(len(time_of_day)):
        mood= random.choices(moods)
        print(f"On {week_days[day]} in the {time_of_day[time]} you were feeling {mood}")
