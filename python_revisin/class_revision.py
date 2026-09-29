# Question 1 — Class, Constructor, Object ⭐
# Create a class called Car.
# Attributes:
# - brand
# - model
# - price
# Take all values from the user inside __init__().
# Method:
# Create a method called display() that prints all the car details.
# Create:
# Create one object and call the display() method.

# class Car:
#     def __init__(self):
#         self.brand=input("Enter brand name: ")
#         self.model=input("Enter Model name: ")
#         self.price=int(input("Enter price: "))
#         print()
#
#     def display(self):
#         print("Brand:",self.brand)
#         print("Name:",self.model)
#         print("Price:",self.price)
#
# c=Car()
# c.display()

# Create a class called Student.
# Requirements:
# 1. In __init__(), take input for:
#    - name
#    - age
#    - mark
# 2. Create a method called display() to print all details.
# 3. Create another method called result():
#    - If mark is greater than or equal to 50, print "Pass"
#    - Otherwise, print "Fail"
# 4. Create an object and call both methods.
class Student:
    def __init__(self):
        self.name=input("Enter student name: ")
        self.age=int(input("Enter age: "))
        self.mark=int(input("Enter Mark: "))
        print()

    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
        print("Mark:",self.mark)

    def result(self):
        if self.mark>=50:
            print("Pass")
        else:
            print("Fail")

a=Student()
a.display()
a.result()