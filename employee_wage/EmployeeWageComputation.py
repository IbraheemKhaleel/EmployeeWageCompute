import random

from employee_wage.IEmployeeWage import IEmployeeWage


class EmployeeWage(IEmployeeWage):
    IS_PRESENT = 1
    IS_PART_TIME = 2
    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4

    '''
    Constructs all the necessary attributes for the employee object.

        Parameters:
            name : string
                name of the company
            maximum_working_days : int
                maximum working days a employee has to work in a month
            maximum_working_hours : int
                maximum working hours a employee has to work in a month
            wage_per_hour
                amount getting paid per hour for employee
    '''

    def __init__(self, name, maximum_working_days, maximum_working_hours, wage_per_hour):
        self.name = name
        self.maximum_working_days = maximum_working_days
        self.maximum_working_hours = maximum_working_hours
        self.wage_per_hour = wage_per_hour

    def __str__(self):
        return "{} {} {} {} ".format(self.name, self.maximum_working_hours, self.maximum_working_days,
                                     self.wage_per_hour)

    '''
    Checking whether employee is present, part time or absent
    
    :parameter: random number between 0 to 2 . 
                if the number is 1, employee present; 2: part time 0;absent
    :returns:   employee working hours based on random number 
    '''

    def employee_check(self, attendance):
        switcher = {
            self.IS_PRESENT: self.FULL_DAY_HOURS,
            self.IS_PART_TIME: self.PART_TIME_HOURS,
        }
        return switcher.get(attendance, 0)

    '''
    calculates daily wage and total wage of the employee
    :parameter : parameters are taken from constructor
    prints the total wage of the respective company's employee
    '''

    def compute_wage(self):
        working_days = 0
        working_hours = 0
        total_wage = 0
        daily_wage = 0
        employee_working_hours = 0
        while working_days < self.maximum_working_days and working_hours < self.maximum_working_hours:  # Calculating wages for month
            random_number = random.randint(0, 2)  # To obtain a random number between 0 and 3
            employee_working_hours = self.employee_check(random_number)
            daily_wage = self.wage_per_hour * employee_working_hours
            total_wage += daily_wage
            working_days += 1
            working_hours += employee_working_hours
        print("Total wage of the company ", self.name, " in the month is ", total_wage)


'''
Declaring main method for running the program

Creating object for the particular company

:parameter:
        name of company : str
        maximum working days : int
        maximum working hours : int
        employee wage per hour : int
'''


def main():
    my_list = []
    reliance = EmployeeWage("reliance", 20, 100, 20)
    bigbazar = EmployeeWage("bigbazar", 25, 75, 15)
    flipkart = EmployeeWage("flipkart", 20, 60, 30)
    dMart = EmployeeWage("dMart", 15, 95, 25)
    my_list.append(reliance)
    my_list.append(bigbazar)
    my_list.append(flipkart)
    my_list.append(dMart)
    reliance.compute_wage()
    bigbazar.compute_wage()
    flipkart.compute_wage()
    dMart.compute_wage()
    for list_object in my_list:
        print(list_object)


'''
Checking whether the module is main, if the it is main module, it will execute the operations
'''

if __name__ == '__main__':
    main()
