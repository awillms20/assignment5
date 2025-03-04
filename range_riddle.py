# Task 1: Your mood today
import random
moods= ['Happy','Sad','Energetic','Calm']
week_days=['Monday','Tuseday','Wednesday','Tursday','Friday']
for weekday in range(len(week_days)):
        mood= random.choices(moods)
        print(f"On {week_days[weekday]} you were feeling{mood}")

