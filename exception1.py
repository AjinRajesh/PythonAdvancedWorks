try:
    num1=int(input("Enter first number: "))
    num2=int(input("Enter second number: "))
    s=num1+num2

except:
    print("Invalid Format")

 #optional
else:
    print("Sum:",s)
finally:
    print("Done")