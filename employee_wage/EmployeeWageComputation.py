import random

from employee_wage.EmployeeWageInfo import EmployeeWageInfo
from employee_wage.IEmployeeWage import IEmployeeWage


class EmployeeWage(IEmployeeWage):
    IS_PRESENT = 1
    IS_PART_TIME = 2
    FULL_DAY_HOURS = 8
    PART_TIME_HOURS = 4
    company_list = []
    company_dictionary = {}

    '''
    :parameter :name of company
                amount getting paid for employee per hour
                maximum amount of hour the employee has to work in a month
                maximum amount of days the employee has to work in a month
    this method adds the all company parameters and calls compute wage method to calculate wages
    :returns company details and total wage
    '''

    def add_company(self, name, employee_wage_per_hour, maximum_working_hour, maximum_working_days):
        employee_wage_info = EmployeeWageInfo(name, employee_wage_per_hour, maximum_working_hour, maximum_working_days)
        self.company_list.append(employee_wage_info)
        print(employee_wage_info)
        return employee_wage_info

    '''
    :parameter : 
                employee_wage_info : object of employee wage info class
    Name of company and its object is stored in a dictionary.
    :returns :  total wage of respective company
    
    '''
    def get_company(self, employee_wage_info):
        return self.company_dictionary.get(employee_wage_info.name)

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

    def compute_wage(self, employee_wage_info):
        working_days = 0
        working_hours = 0
        total_wage = 0
        daily_wage = 0
        employee_working_hours = 0
        while working_days < employee_wage_info.maximum_working_days \
                and working_hours < employee_wage_info.maximum_working_hours:  # Calculating wages for month
            random_number = random.randint(0, 2)  # To obtain a random number between 0 and 3
            employee_working_hours = self.employee_check(random_number)
            daily_wage = employee_wage_info.wage_per_hour * employee_working_hours
            total_wage += daily_wage
            working_days += 1
            working_hours += employee_working_hours
        print("Total wage of the company ", employee_wage_info.name, " in the month is ", total_wage)
        self.company_dictionary[employee_wage_info.name] = total_wage


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
    employee_wage = EmployeeWage()
    employee_wage.add_company("reliance", 20, 100, 20)
    employee_wage.add_company("bigbazar", 25, 75, 15)
    employee_wage.add_company("flipkart", 20, 60, 30)
    employee_wage.add_company("dMart", 15, 95, 25)
    for _ in EmployeeWage.company_list:
        employee_wage.compute_wage(_)
    company_name = input("Enter company name")
    print(employee_wage.company_dictionary.get(company_name))  # finding total wage for the particular company


'''
Checking whether the module is main, if the it is main module, it will execute the operations
'''

if __name__ == '__main__':
    main()
