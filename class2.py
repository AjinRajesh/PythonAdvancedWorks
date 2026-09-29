#Define a class name Employee with attributes empid,name,age,place,salary,designation
#and methods getSalary()and showpersondetails() #create an employee and call the methods
class Employee:
    def __init__(self):
        print("Employee details")
        self.empid=int(input("Enter employee Id: "))
        self.name=input("Enter employee Name: ")
        self.age=int(input("Enter employee age: "))
        self.place=input("Enter employee place: ")
        self.salary=int(input("Enter employee Salary: "))
        self.designation=input("Enter employee designation: ")
        print()

    def getSalary(self):
        print(f"Salary of {self.name} is {self.salary}")
        print()

    def showpersondetails(self):
        print(f"Employee id: {self.empid}")
        print(f"Employee name: {self.name}")
        print(f"Employee age: {self.age}")
        print(f"Employee place: {self.place}")
        print(f"Employee salary: {self.salary}")
        print(f"Employee designation: {self.designation}")

e1=Employee()
e1.getSalary()
e1.showpersondetails()