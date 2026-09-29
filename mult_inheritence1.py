class Hospital:
    def __init__(self):
        self.hos_name=input("Enter hospital name: ")
        self.location=input("Enter location: ")
        self.phone=int(input("Enter phone no: "))

    def disp_hospital(self):
        print(f"Hospital:{self.hos_name:6}  location:{self.location:6}  Phone:{self.phone:6}")
        print()

class Department:
    def __init__(self):
        self.dept_name=input("Enter Department name: ")
        self.doctor_name=input("Enter Doctor Name: ")

    def disp_department(self):
        print(f"Department:{self.dept_name:6}  Doctor name:{self.doctor_name:6}")
        print()

class Patient(Hospital,Department):
    def __init__(self):
        Hospital.__init__(self)
        Department.__init__(self)
        self.patient_name=input("Enter patient name: ")
        self.age=int(input("Enter patient age: "))
        self.admission_date=input("Enter date of admission: ")
        self.bedno=int(input("Enter bed number: "))
        self.disch_date=""

    def set_discharge(self):
        self.disch_date=input("Enter discharge date:")
        print()

    def full_sumary(self):
        Hospital.disp_hospital(self)
        Department.disp_department(self)
        print(f"Patient name:{self.patient_name:6}  age:{self.age:6}  admission date:{self.admission_date:6}  bed numb:{self.bedno:6}  discharge date:{self.disch_date:6}")
        print()

p=Patient()
p.set_discharge()
p.full_sumary()