class Company:
    def __init__(self):
        self.company_name=input("Enter company name: ")
        self.location=input("Enter location: ")

    def display_company(self):
        print("Company name:",self.company_name)

class Employee(Company):
    def __init__(self):
        super().__init__()
        self.empid=int(input("Enter EmpID: "))
        self.name=input("Enter emp name: ")
        self.designation=input("Enter designation: ")
        self.salary=int(input("Enter salary: "))
        print()

    def display_details(self):
        self.display_company()
        print("Location:",self.location)
        print("EmID:",self.empid)
        print("Emp name:", self.name)
        print("Emp designation:", self.designation)
        print("Emp Salary:",self.salary)
        print()

    def update_salary(self):
        self.salary=self.salary + (0.1 * self.salary)
        self.display_details()

e=Employee()
e.display_details()
e.update_salary()