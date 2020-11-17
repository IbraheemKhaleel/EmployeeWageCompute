from employee_wage.EmployeeWageComputation import EmployeeWage


def test_employee_wage_company_name():
    employee_wage = EmployeeWage()
    company = employee_wage.add_company("reliance", 20, 100, 20)
    assert company.name == "reliance"


def test_employee_wage_maximum_working_hours():
    employee_wage = EmployeeWage()
    company = employee_wage.add_company("bigbazar", 25, 75, 15)
    assert company.maximum_working_hours == 75


def test_employee_wage_maximum_working_days():
    employee_wage = EmployeeWage()
    company = employee_wage.add_company("flipkart", 20, 60, 30)
    assert company.maximum_working_days == 30


def test_employee_wage_wage_per_hour():
    employee_wage = EmployeeWage()
    company = employee_wage.add_company("dMart", 15, 95, 25)
    assert company.wage_per_hour == 15


def test_employee_check():
    employee_wage = EmployeeWage()
    assert employee_wage.employee_check(1) == 8


def test_given_company_list_should_calculate_total_employee_wage_for_each_company():
    employee_wage = EmployeeWage()
    employee_wage.add_company("reliance", 20, 100, 20)
    employee_wage.add_company("bigbazar", 25, 75, 15)
    employee_wage.add_company("flipkart", 20, 60, 30)
    employee_wage.add_company("dMart", 15, 95, 25)
    for _ in EmployeeWage.company_list:
        employee_wage.compute_wage(_)
    assert True
