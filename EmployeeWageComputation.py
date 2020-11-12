import random

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
totalWage = 0
employeeWorkingHours = 0
randomNumber = random.randrange(0, 3)  # To obtain a random number between 0 and 2
if randomNumber == 1:
    print("employee is present")
    employeeWorkingHours = FULL_DAY_HOURS
elif randomNumber == 2:
    print("employee is part time")
    employeeWorkingHours = 4
else:
    print("employee is absent")
totalWage = WAGE_PER_HOUR * employeeWorkingHours
print(totalWage)
