# 1.Create a class named Circle with an attribute radius. Use a constructor to
# initialize the radius by accepting input from the user. Define the following methods:
# #
# getarea() – to calculate and display the area of the circle.
# getperimeter() – to calculate and display the perimeter (circumference) of the circle.
#
# Create an object of the Circle class and call both methods to display the results.
class Circle:
    def __init__(self):
        self.radius=int(input("Radius: "))
        print()

    def getarea(self):
        print("Area of circle:",3.14*self.radius*self.radius)
        print()

    def getperimeter(self):
        print("Perimeter of circle:",2*3.14*self.radius)
        print()

c=Circle()
c.getarea()
c.getperimeter()

#
# 2.Create a class named Account with attributes acctnumber, acctname, and balance.
# Initialize these values using a constructor by taking input from the user. Define the following methods:
#
# withdraw() – to withdraw an amount from the account and update the balance.
# deposit() – to deposit an amount into the account and update the balance.
# showbalance() – to display the current balance of the account.
#
# Create an object of the class and call the methods to perform withdrawal and deposit
# operations and display the updated balance.
class Account:
    def __init__(self):
        self.acctnumber=int(input("Account Number: "))
        self.acctname=input("Acct name: ")
        self.balance=int(input("Balance: "))
        print()

    def withdraw(self):
        withdraw=int(input("Enter amount to withdraw: "))
        if withdraw>self.balance:
            print("Insufficient Balance")
        else:
            self.balance=self.balance-withdraw
            self.showbalance()

    def deposit(self):
        deposit=int(input("Enter amount to deposit: "))
        self.balance+=deposit
        self.showbalance()

    def showbalance(self):
        print("Current Balance:",self.balance)
        print()

c1=Account()
c1.showbalance()
c1.deposit()
c1.withdraw()

