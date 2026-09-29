#write a menu driven code for bank operations
#using class and list
#1.Create a new account
#2.withdraw
# 3.deposit
# 4.showbalnace
# 5.exit

class Bank:
    def __init__(self):
        self.account_no=int(input("Enter Account Number: "))
        self.name=input("Enter account name: ")
        self.balance=int(input("Enter balance: "))
        print()

    def withdraw(self):
        amount=int(input("Enter amount to withdraw: "))
        if amount>self.balance:
            print("Insufficient balance")
        else:
            self.balance-=amount
            self.showbalance()

    def showbalance(self):
        print(f"Balance of {self.account_no}: {self.balance}")
        print()

    def deposit(self):
        amount=int(input("Enter amount to deposit: "))
        self.balance+=amount
        self.showbalance()

l=[]
while True:
    ch = int(input("1.Create a new account\n2.withdraw\n3.deposit\n4.showbalance\n5.exit\nEnter choice: "))
    if ch==1:
        a=Bank()
        l.append(a)
        print(l)
    elif ch==2:
        n=int(input("Enter Account no to withdraw:" ))
        for i in l:
            if i.account_no==n:
                i.withdraw()
    elif ch==3:
        n=int(input("Enter account number to deposit: "))
        for i in l:
            if i.account_no==n:
                i.deposit()
    elif ch==4:
        n=int(input("Enter account number to show balance: "))
        for i in l:
            if i.account_no==n:
                i.showbalance()
    elif ch==5:
        exit()
    else:
        print("Invalid Choice")