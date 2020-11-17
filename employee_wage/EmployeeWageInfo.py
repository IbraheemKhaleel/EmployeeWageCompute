class EmployeeWageInfo:

    """
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
    """

    def __init__(self, name, wage_per_hour, maximum_working_hours, maximum_working_days ):
        self.name = name
        self.maximum_working_days = maximum_working_days
        self.maximum_working_hours = maximum_working_hours
        self.wage_per_hour = wage_per_hour

    def __str__(self):
        return "{} {} {} {} ".format(self.name, self.maximum_working_hours, self.maximum_working_days,
                                     self.wage_per_hour)
