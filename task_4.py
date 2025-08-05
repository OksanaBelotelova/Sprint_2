class EmployeeSalary:
    hourly_payment = 400

    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = (f"{name}@email.com")
        return cls(name, hours, rest_days, email)

    @classmethod
    def set_hourly_payment(cls, value):
        hourly_payment = value

    def salary(self):
        salary = self.hours * self.hourly_payment
        return salary


# данные для проверки:
employee1 = EmployeeSalary.get_hours('Tom', 2, 'tom@email.com')
print(employee1.hours)
employee2 = EmployeeSalary.get_email('Mike', 8, 6)
print(employee2.email)
print(employee1.salary())
print(employee2.salary())
EmployeeSalary.hourly_payment = 500
print(employee1.salary())
print(employee2.salary())
