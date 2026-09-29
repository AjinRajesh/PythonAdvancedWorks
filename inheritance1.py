# class Parent:
#     def m1(self):
#         print("Method M1 in parent class")
#
#     def m2(self):
#         print("In parent class method m2")
#
# class Child(Parent):
#     def m3(self):
#         print("In child class m3")
#
# s=Child()
# s.m1()
# s.m2()
# s.m3()

#-------------------------------------------------------------
class Parent:
    def m1(self):
        print("In parent class m1")

    def m2(self):
        print("In parent class method m2")

class Child(Parent):
    def m1(self):
        super().m1()# to call parent m1 also
        print("In child class m1")         # method overriding

    def m3(self):
        print("In child class m3")

s=Child()
s.m1()# child class's m1 has priority, to call parent class's also we use super()
s.m2()
s.m3()