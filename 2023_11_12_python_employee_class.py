class Employee:
    def __init__(self):
        self.hours = 0
        self.employee_number = 0
        self.office_number = 0
        self.name = ""
        self.birthdate = (0, 0, 0)

    def add_hours(self, x):
        if x < 0:
            raise ValueError("Hours to be added cannot be negative.")
        self.hours += x

    def set_employee_number(self, x):
        if not isinstance(x, int):
            raise TypeError("Employee number must be an integer.")
        self.employee_number = x

    def set_office_number(self, x):
        if not (100 <= x <= 500):
            raise ValueError("Office number must be between 100 and 500.")
        self.office_number = x

    def set_name(self, x):
        if not x:
            raise ValueError("Name cannot be empty.")
        for char in ['_', '.', '-']:
            x = x.replace(char, "")
        self.name = x

    def set_birthdate(self, m, d, y):
        if not (1 <= m <= 12):
            raise ValueError("Month must be between 1 and 12.")
        if not (1 <= d <= 31):  # Simplified check, doesn't account for different days in each month
            raise ValueError("Day must be between 1 and 31.")
        self.birthdate = (m, d, y)

# Example usage:
employee = Employee()
try:
    employee.add_hours(-5)
except ValueError as e:
    print(e)

try:
    employee.set_employee_number("A123")
except TypeError as e:
    print(e)

try:
    employee.set_office_number(99)
except ValueError as e:
    print(e)

try:
    employee.set_name("")
except ValueError as e:
    print(e)

try:
    employee.set_birthdate(0, 32, 1990)
except ValueError as e:
    print(e)
