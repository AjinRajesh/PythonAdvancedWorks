try:
    num1 = int(input("Enter first number: "))
    num2 = int(input("Enter second number: "))
    r = num1/num2
    print("Result:",r)

except ZeroDivisionError:
    print("Division by zero not possible")
except ValueError:
    print("Invalid format")
except:#general code if any exception other than above two
    print("Error")

