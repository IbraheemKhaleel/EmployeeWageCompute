import random


class EmployeeWage:
    WAGE_PER_HOUR = 20
    MAXIMUM_WORKING_DAYS = 20
    MAXIMUM_WORKING_HOURS = 100

    def compWage(self):
        IS_PRESENT = 1
        IS_PART_TIME = 2
        FULL_DAY_HOURS = 8
        PART_TIME_HOURS = 4
        workingDays = 0
        workingHours = 0
        totalWage = 0
        dailyWage = 0
        employeeWorkingHours = 0
        while workingDays < self.MAXIMUM_WORKING_DAYS and workingHours < self.MAXIMUM_WORKING_HOURS:  # Calculating wages for month
            randomNumber = random.randrange(0, 3)  # To obtain a random number between 0 and 3
            if randomNumber == IS_PRESENT:
                employeeWorkingHours = 8
            elif randomNumber == IS_PART_TIME:
                employeeWorkingHours = 4
            else:
                employeeWorkingHours = 0
            dailyWage = self.WAGE_PER_HOUR * employeeWorkingHours
            totalWage += dailyWage
            workingDays += 1
            workingHours += employeeWorkingHours
        print("Total wage of the month is ", totalWage)


employeeWage = EmployeeWage()
employeeWage.compWage()
