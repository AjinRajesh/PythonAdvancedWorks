# 1. List + Function + Multiple Returns
# Define a function that takes a list of numbers and returns:
# - Count of even numbers
# - Count of odd numbers
# - Sum of positive numbers
def fun1(l):
    even=0
    odd=0
    tot=0
    for i in l:
        if i%2==0:
            even+=1
        elif i%2!=0:
            odd+=1
        if i>0:
            tot+=i
    return even,odd,tot

l = [12, -5, 7, 10, -8, 15, 20]
ev,odd,tot=fun1(l)
print("Count of even numbers: ",ev)
print("Count of odd numbers: ",odd)
print("sum of positive numbers: ",tot)


# 2. String + Dictionary + Function
# Define a function that takes a string and returns a dictionary where:
# - Keys are the unique characters
# - Values are their frequency
# - Ignore spaces
def fun2(s):
    dic={}
    for i in s:
        if i==" ":
            continue
        dic[i]=s.count(i)
    return dic

print()
s = "banana apple"
print(fun2(s))


# 3. List + Function
# Define a function that takes a list and returns a new list containing the second largest unique number.
def fun3(l):
    l=list(set(l))
    print("list of unique elements:",l)
    new=[]
    if l[0]>l[1]:
        largest=l[0]
        sec=l[1]
    else:
        largest=l[1]
        sec=l[0]
    for i in l[2:]:
        if i>largest:
            sec=largest
            largest=i
    new.append(sec)
    return new

l = [12, 45, 67, 45, 89, 67, 23]
print()
print("List containing second largest element:",fun3(l))


# 4. String + Loop + Function
# Define a function that takes a string and returns a new string
# where each word is reversed, but the order of the words remains the same.
def fun4(s):
    new=''
    for i in s.split():
        rev = ""
        for j in str(i):
            rev=j+rev
        new=new+rev+" "
    return new

s = "python is easy"
print()
print("string after reversing each word:",fun4(s))