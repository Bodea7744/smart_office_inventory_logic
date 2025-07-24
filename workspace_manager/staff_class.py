# Staff Class – office personnel representation

class Staff:
    def __init__(self, name, email, salary, location):
        self.name = str(name)
        self.email = str(email)
        self.salary = float(salary)
        self.location = str(location)

    def check_email(self):
        return "@" in self.email

    def increase_salary(self, percentage):
        self.salary *= 1 + (percentage / 100)