#define a class named Student with attributes rollno,mark1,mark2,mark3 and metthods
#display() to display roll no and total mark of a student.
#create 2 student object and call the methods
class Student:
    def __init__(self):
        self.rollno=int(input("Roll no = "))
        self.mark1 = int(input("Mark1: "))
        self.mark2 = int(input("Mark2: "))
        self.mark3 = int(input("Mark3: "))
        print()

    def display(self):
        tot=self.mark1+self.mark2+self.mark3
        print("Roll no:",self.rollno)
        print("Total mark:",tot)
        print()

s1=Student()
s2=Student()
s1.display()
s2.display()