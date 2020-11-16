from abc import ABC, abstractclassmethod, abstractmethod


class IEmployeeWage:

    # abstract method for compute wage method is declared
    @abstractmethod
    def compute_wage(self):
        pass

    # abstract method for attendance check is declared
    @abstractmethod
    def employee_check(self, attendance):
        pass



