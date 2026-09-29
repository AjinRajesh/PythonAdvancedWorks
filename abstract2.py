#create an abstract class employee with an abstract method calculate_salary()
# create two subclasses
# -FullTimeEmployee
# -PartTimeEmployee
# Each class should calculate salary differently.

from abc import ABC,abstractmethod

class Employee(ABC):
    def __init__(self):
        self.name=input("Enter name: ")
        self.age=int(input("Age: "))
        self.empid=int(input("Employee ID: "))

    @abstractmethod
    def calculate_salary(self):
        pass

class FulltimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.monthly_salary=int(input("Monthly salary: "))

    def calculate_salary(self):
        print("Total Salary:",self.monthly_salary*12)
        print()

class ParttimeEmployee(Employee):
    def __init__(self):
        super().__init__()
        self.hours=int(input("Enter Hours worked: "))
        self.rate=int(input("Enter Rate per hour: "))

    def calculate_salary(self):
        print("Total salary:",self.rate*self.hours)
        print()

f=FulltimeEmployee()
f.calculate_salary()

p=ParttimeEmployee()
p.calculate_salary()