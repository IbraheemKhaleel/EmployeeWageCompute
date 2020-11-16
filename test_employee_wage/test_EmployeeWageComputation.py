from employee_wage.EmployeeWageComputation import EmployeeWage


def test_employee_wage_company_name():
    reliance = EmployeeWage("reliance", 15, 95, 25)
    assert reliance.name == "reliance"


def test_employee_wage_maximum_working_hours():
    bigbazar = EmployeeWage("bigbazar", 25, 75, 15)
    assert bigbazar.maximum_working_hours == 75


def test_employee_wage_maximum_working_days():
    flipkart = EmployeeWage("flipkart", 20, 60, 30)
    assert flipkart.maximum_working_days == 20


def test_employee_wage_wage_per_hour():
    dMart = EmployeeWage("dMart", 15, 95, 25)
    assert dMart.wage_per_hour == 25


def test_employee_check():
    flipkart = EmployeeWage("flipkart", 20, 60, 30)
    assert flipkart.employee_check(2) == 4
