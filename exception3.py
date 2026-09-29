# write a program that takes a number as input from user and finds the factorial of that number
# using math.factorial().use a try -except block to handle the value error if user inputs a
# number/character input
while True:
    try:
        num=int(input("Enter number: "))
        import math
        fact=math.factorial(num)
        print("Factorial:",fact)
        break
    # except:
    #     print("Invalid input format")
    except Exception as e:
        print(e)


# Write a Python program to create a simple calculator that performs addition, subtraction, multiplication,
# and division based on user choice. Handle invalid inputs and division by zero using exception handling.

while True:
    try:
        ch=int(input("1.Addition\n2.Subtraction\n3.Multiplication\n4.Division\n5.Exit\nEnter Choice: "))
        if ch==1:
            n1=int(input("Enter first number: "))
            n2=int(input("Enter second number: "))
            print("Sum:",n1+n2)
        elif ch==2:
            n1=int(input("Enter first number: "))
            n2=int(input("Enter second number: "))
            print("Difference:",n1-n2)
        elif ch==3:
            n1=int(input("Enter first number: "))
            n2=int(input("Enter second number: "))
            print("Product:",n1*n2)
        elif ch==4:
            n1=int(input("Enter first number: "))
            n2=int(input("Enter second number: "))
            print("Quotient:",n1/n2)
        elif ch==5:
            break
        else:
                print("Wrong number")
    # except ValueError:
    #     print("Invalid Input")
    # except ZeroDivisionError:
    #     print("Division By zero not possible")
    # except Exception:
    #     print("Error")
    except ValueError as v:
        print(v)
    except ZeroDivisionError as z:
        print(z)
    except Exception as e:
        print(e)

# write a program to open a file (text file) in read mode
# if the file does not exist catch the file exception print the error message file does not
# exist
try:
    file_name = input("Enter the file name: ")

    f = open(file_name, "r")

    print(f.read())

    f.close()

# except FileNotFoundError:
#     print("File does not exist")
except FileNotFoundError as f:
    print(f)


#Given a Dictionary
#
# d={"name':"arun","age":23,"place":"ekm"}
# Write a program to ask the user to enter a key and display its value.
# Handle KeyError if key does not exist
d = {"name": "arun", "age": 23, "place": "ekm"}

try:
    key = input("Enter the key: ")
    print("Value:", d[key])

# except KeyError:
#     print("Key does not exist")
except KeyError as k:
    print(k)