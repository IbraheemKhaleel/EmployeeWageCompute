import random

WAGE_PER_HOUR = 20
FULL_DAY_HOURS = 8
totalWage = 0
randomNumber = random.randrange(0, 2)  # To obtain a random number between 0 and 1
if randomNumber == 1:
    print("employee is present")
else:
    print("employee is absent")
totalWage = WAGE_PER_HOUR * FULL_DAY_HOURS
print(totalWage)
