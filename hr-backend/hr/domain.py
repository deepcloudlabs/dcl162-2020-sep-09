from enum import Enum


class Department(Enum):
    SALES = 1
    IT = 2
    FINANCE = 3


class Employee:
    def __init__(self, identity, fullName, iban, photo, birthYear, salary=50000, department=Department.IT,
                 fulltime=True):
        self.identity = identity
        self.fullName = fullName
        self.iban = iban
        self.photo = photo
        self.birthYear = birthYear
        self.salary = salary
        self.department = department
        self.fulltime = fulltime
