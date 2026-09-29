# Write a menu-driven Python program using a class Student
#     to perform the following operations:
#
# 1Add Student(roll no,name,marks)
# 2Update Marks
# 3Display All Student Details
# 4Search Student by Roll Number
# 5Delete Student
# 6Exit
# Store student records in a list and perform all operations using the student's roll number.
class Student:
    def __init__(self):
        self.rollno=int(input("Enter Roll no: "))
        self.name=input("Enter name: ")
        self.mark=int(input("Enter mark: "))
        print()

    def update(self):
        new=int(input("Enter new mark: "))
        self.mark=new
        print()

    def display(self):
        print(f"{self.rollno:3} {self.name:10}  {self.mark:3}")
        print()

l=[]
while True:
    ch=int(input("1.Add student\n2.Update Marks\n3.Display All Student Details\n4.Search Student by Roll Number\n5.Delete Student\n6.Exit\nEnter Choice: "))
    if ch==1:
        a=Student()
        l.append(a)

    elif ch==2:
        n=int(input("Enter Roll no to update mark: "))
        for i in l:
            if i.rollno==n:
                i.update()
                break
        else:
            print("Roll no not found in DB")

    elif ch==3:
        for i in l:
            i.display()

    elif ch==4:
        n = int(input("Enter Roll no to show specific student detail: "))
        for i in l:
            if i.rollno == n:
                i.display()
                break
        else:
            print("Roll no not found in DB")

    elif ch==5:
        n = int(input("Enter Roll no to delete student: "))
        for i in l:
            if i.rollno == n:
                l.remove(i)
                break
        else:
            print("No such Student")

    elif ch==6:
        exit()
    else:
        print("Invalid Operation")

