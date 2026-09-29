def add():
    n1=int(input("Enter number1: "))
    n2=int(input("Enter number2: "))
    print("Sum =",n1+n2)

def sub():
    n1=int(input("Enter number1: "))
    n2=int(input("Enter number2: "))
    print("Difference =",n1-n2)

def mul():
    n1=int(input("Enter number1: "))
    n2=int(input("Enter number2: "))
    print("Product =",n1*n2)

def div():
    n1=int(input("Enter number1: "))
    n2=int(input("Enter number2: "))
    print("Quotient =",n1/n2)

while(True):
    n=int(input("1.add\n2.su\n3.mul\n4.div\n5.exit\nEnter choice: "))
    if n==1:
        add()
    elif n==2:
        sub()
    elif n==3:
        mul()
    elif n==4:
        div()
    elif n==5:
        exit()
    else:
        print("wrong input")