# class Person:
#     def __init__(self):
#         self.name=input("Enter name: ")
#         self.age=int(input("Enter age: "))
#         print()
#
# class Student(Person):
#     pass
#
# s=Student() #since no init in Student class parent class init works

# class Person:
#     def __init__(self):
#         self.name=input("Enter name: ")
#         self.age=int(input("Enter age: "))
#         print()
#
# class Student(Person):
#     def __init__(self):
#         super().__init__()
#         self.roll_no=int(input("Enter Roll number: "))
#         self.course=input("Enter course: ")
#         self.mark=int(input("Enter marks: "))
#
#
# s=Student()#here child class(Student class) __init__ works, but we can initialize parent class init using super


class Person:
    def __init__(self):
        self.name=input("Enter name: ")
        self.age=int(input("Enter age: "))
        print()

    def show(self):
        print(self.name,self.age,end=" ")

class Student(Person):
    def __init__(self):
        super().__init__()
        self.roll_no=int(input("Enter Roll number: "))
        self.course=input("Enter course: ")
        self.mark=int(input("Enter marks: "))
    print()
    def show(self):
        super().show()
        print(self.roll_no,self.course,self.mark)
        print()

    def updatemark(self):
        self.mark=int(input("Enter new mark:"))
        self.show()

s=Student()
s.show()
s.updatemark()
