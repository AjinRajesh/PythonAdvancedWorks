#Ask the user to enter a number.if the number is less than or equal to 0,
# raise a ValueError with the message "Number must be Positive"
try:
    num=int(input("Enter a number: "))
    if num<=0:
        raise ValueError("Number Must be Positive")
    else:
        print(num)
except ValueError as e:
    print(e)



#Ask the user to enter a password.if its length is less than 8 characters ,raise
#a customexception InvalidPasswordError with the message ("Password should be 8
# characters")
class InvalidPasswordError(Exception):
    pass
try:
    pwd=input("Enter Password: ")
    if len(pwd)<8:
        raise InvalidPasswordError("InvalidPasswordError")
    else:
        print("strong Password")
except InvalidPasswordError as e:
    print(e)



#Ask the user to enter an amount and if the amount<balance ,raise customException
#InsuffientBalanceError with the message("Not Enough Balance.Transaction Failed")
class InsufficientBalanceError(Exception):
    pass
try:
    amount=int(input("Enter amount: "))
    Balance=5000
    if amount>Balance:
        raise InsufficientBalanceError("InsufficientBalanceError Occured")
    else:
        print("Remaining:",Balance-amount)
except InsufficientBalanceError as e:
    print(e)