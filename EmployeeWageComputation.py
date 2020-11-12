import random


class EmployeeWage:

    def compWage(self, name, MAXIMUM_WORKING_DAYS, MAXIMUM_WORKING_HOURS, WAGE_PER_HOUR):
        IS_PRESENT = 1
        IS_PART_TIME = 2
        FULL_DAY_HOURS = 8
        PART_TIME_HOURS = 4
        workingDays = 0
        workingHours = 0
        totalWage = 0
        dailyWage = 0
        employeeWorkingHours = 0
        while workingDays < MAXIMUM_WORKING_DAYS and workingHours < MAXIMUM_WORKING_HOURS:  # Calculating wages for month
            randomNumber = random.randrange(0, 3)  # To obtain a random number between 0 and 3
            if randomNumber == IS_PRESENT:
                employeeWorkingHours = 8
            elif randomNumber == IS_PART_TIME:
                employeeWorkingHours = 4
            else:
                employeeWorkingHours = 0
            dailyWage = WAGE_PER_HOUR * employeeWorkingHours
            totalWage += dailyWage
            workingDays += 1
            workingHours += employeeWorkingHours
        print("Total wage of the company ", name, " in the month is ", totalWage)


employeeWage = EmployeeWage()    # creating an object
employeeWage.compWage("Dmart", 20, 100, 20)     # details of company dmart
employeeWage.compWage("FlipKart", 30, 80, 30)   # details of flipkart company
employeeWage.compWage("Amazon", 15, 90, 30)     # details of Amazon company
