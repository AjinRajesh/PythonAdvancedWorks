# class Person:                        #<------|
#     def __init__(self,n,a):                 #|
#         self.name=n                        #|------ #Class Definition
#         self.age=a                          #|
#     def show(self):                         #|
#         print(self.name, self.age)   #<------|

#object creation
# p1=Person("Ajin",23)
# p2=Person("Alan",22)
# p1.show()
# p2.show()

#---------Dynamic Input--------------
class Person:
    def __init__(self):  #__init__() used to create and initialize current object properties/attributes
        self.name=input("Enter the name: ")
        self.age=int(input("Enter the age: "))
    def show(self): #Self represents current object
        print(self.name, self.age)

p1=Person()#Creates obj of class person, it will call __init__() automatically
p2=Person()#Creates obj of class person, it will call __init__() automatically
p1.show()
p2.show()