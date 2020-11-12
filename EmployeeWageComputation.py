import random

WAGE_PER_HOUR = 20
MAXIMUM_WORKING_DAYS = 20
FULL_DAY_HOURS = 8
PART_TIME_HOURS = 4
IS_PRESENT = 1
IS_PART_TIME = 2
workingDays = 0
totalWage = 0
dailyWage = 0
employeeWorkingHours = 0
randomNumber = random.randrange(0, 3)  # To obtain a random number between 0 and 2


def calculateWages(choice):  # Calculating wages with switcher
    switcher = {
        IS_PRESENT: 8,
        IS_PART_TIME: 4,
    }
    return switcher.get(randomNumber, 0)


while workingDays <= MAXIMUM_WORKING_DAYS:      # Calculating wages for month
    employeeWorkingHours = calculateWages(randomNumber)
    dailyWage = WAGE_PER_HOUR * employeeWorkingHours
    totalWage += dailyWage
    workingDays += 1
print("Total wage of the month is ", totalWage)
