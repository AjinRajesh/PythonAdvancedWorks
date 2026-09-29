# #1. Prime numbers using a function
# #Return a new list containing only the prime numbers.
# def prime_numbers(l):
#     new=[]
#     for i in l:
#         if i<=1:
#             continue
#         for j in range(2,i):
#             if i%j==0:
#                 break
#         else:
#             new.append(i)
#     return new
#
# l = [-1,0,1,2,12, 17, 23, 34, 41, 50, 53, 60]
# print("List of Prime Numbers:",prime_numbers(l))
# print()
#
#
# # #2. Armstrong numbers
# # Write a program to print all Armstrong numbers between 100 and 999.
# for i in range(100,1000):
#     tot=0
#     for j in str(i):
#         tot+=int(j)**len(str(i))
#     if tot==i:
#         print(i,end=" ")
# print("\n")
#
#
# #3. List comprehension
# # Given:
# l = [23, 56, -12, 89, -34, -23, 67, 9.7, 4.5, 'hello']
# # Using list comprehension, create:
# # 1. A list of positive numbers
# new=[i for i in l if(type(i)==int or type(i)==float) and i>0]
# print(new)
# # 2. A list of negative numbers
# new=[i for i in l if(type(i)==int or type(i)==float) and i<0]
# print(new)
# # 3. A list of float values
# new=[i for i in l if type(i)==float]
# print(new)
# # 4. A list of string values
# new=[i for i in l if type(i)==str]
# print(new)
#
#
# # 4. Lambda + map() / filter() / reduce()
# # Given:
# l = [12, -4, 78, -34, 90, 45, 16, 26, -2, -11, 3]
# # Using the appropriate higher-order functions:
# print("\n")
# # 1. Create a list containing squares of all numbers.
# print(list(map(lambda n:n**2,l)))
# # 2. Create a list containing positive numbers.
# p=list(filter(lambda x:x>0,l))
# print(p)
# # 3. Find the sum of all positive even numbers.
# pe=list(filter(lambda x:x>0 and x%2==0,l))
# import functools
# print("Sum of positive even:",functools.reduce(lambda a,b:a+b,pe,0))
# # 4. Find the count of negative numbers.
# n=list(filter(lambda x:x<0,l))
# print("Count of negative integers:",functools.reduce(lambda a,b:a+1,n,0))
# # Don't use normal for loops for these.
#
#
# # 5. Nested-loop pattern
# # Print:
# #         *
# #       * *
# #     * * *
# #   * * * *
# # * * * * *
# #   * * *
# #     * *
# #       *
# # Topics: nested loops + range() + spaces.
# print("\n")
# k=8
# for i in range(1,6):
#     for p in range(k):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     k-=2
#     print()
# #second part
# k=2
# for i in range(3,0,-1):
#     for p in range(k):
#         print(end=" ")
#     for j in range(i):
#         print("*",end=" ")
#     print()
#     k+=2
# print("\n")
#
# #---------new questions-----------
# # 6. Function + list + multiple conditions
# # Define:
# # def analyze(l):
# # Given:
# # l = [12, -5, 8, 91, 34, -20, 67, 3, 50]
# # Return:
# # - count of positive even numbers
# # - count of negative numbers
# # - sum of numbers between 10 and 50 inclusive
# # - largest number
# # Example output:
# # Positive even count: ...
# # Negative count: ...
# # Sum between 10 and 50: ...
# # Largest: ...
# def analyze(l):
#     pos=0
#     neg=0
#     net=0
#     for i in l:
#         if i>0 and i%2==0:
#             pos+=1
#         elif i<0:
#             neg+=1
#         if i>=10 and i<=50:
#             net+=i
#     l.sort()
#     largest=l[-1]
#     return pos,neg,net,largest
#
# l = [12, -5, 8, 91, 34, -20, 67, 3, 50]
# p,n,net,lar=analyze(l)
# print("Positive even count:",p)
# print("Negative count:",n)
# print("Sum of numbers between 10 and 50:",net)
# print("Largest number:",lar)
# print("\n")
#
#
# # 7. String comprehension ⭐
# # Given:
# s = "Python is very easy and powerful"
# # Using list comprehension, create a list containing the first letter of every word.
# # Expected:
# # ['P', 'i', 'v', 'e', 'a', 'p']
# # Then create another list containing only words whose length is greater than 4.
# first=[i[0] for i in s.split()]
# print(first)
# new=[i for i in s.split() if len(i)>4]
# print(new)
# print("\n")
#
#
# # 8. filter() + map()
# # Given:
# l = [12, 5, 18, 23, 40, 7, 60, 33]
# # Using filter() and map():
# # 1. Select numbers greater than 20.
# # 2. Create a new list containing their squares.
# # Expected:
# # [1600, 3600, 1089]
# # Think:
# # filter → select
# #        ↓
# # map → transform
# num=list(filter(lambda x:x>20,l))
# print(num)
# new=list(map(lambda a:a**2,num))
# print(new)
# print("\n")
#
# # 9. Lambda + reduce() ⭐
# # Given:
# l = [5, 10, 15, 20]
# # Using reduce():
# # 1. Find the sum.
# print("Sum:",functools.reduce(lambda a,b:a+b,l,0))
# # 2. Find the product.
# print("Product:",functools.reduce(lambda a,b:a*b,l,1))
# # 3. Find the largest number.
# print("largest:",functools.reduce(lambda a,b:a if a>b else b,l))
# # Don't use sum(), max(), or a normal loop.
#
#
# # 10. ⭐ Combined function question
# # Define a function:
# # def process_numbers(l):
# # Given:
# # l = [12, 45, 7, 20, 33, 8, 91, 50, 6]
# # The function should:
# # 1. Create a new list containing the even numbers.
# # 2. Create another list containing the squares of those even numbers.
# # 3. Count how many numbers are greater than 30.
# # 4. Find the sum of all odd numbers.
# # 5. Return all four results.
# # Restriction: Use a combination of loops, conditions
# # and list comprehension. Don't use map/filter/reduce for this one.
#
# #--------------------------------------------------------------
# # 1. Alternating sum — Function + loop
# # Define a function alternate_sum(l) that takes a list of numbers and calculates:
# # first - second + third - fourth + fifth...
# # For example:
# # l = [10, 5, 8, 3, 6]
# # Expected:
# # 10 - 5 + 8 - 3 + 6 = 16
# # Don't use sum().
from select import select


def alt_sum(l):
    net=0
    for i in range(0,len(l)):
        if i==0:
            net+=l[0]
        elif i%2!=0:
            net-=l[i]
        else:
            net+=l[i]
    return net

l=[10,5,8,3,6]
print("Alternate Sum=",alt_sum(l))
print("\n")


#2. Number transformation — map() + lambda
# Given:
l = [3, 8, 11, 14, 21, 26]
# Using map() and a lambda function:
# - If a number is even, replace it with its square.
# - If a number is odd, replace it with its cube.
# Expected:
# [27, 64, 1331, 196, 9261, 676]
# This tests whether you can put an if-else expression inside a lambda.
print("Output:",list(map(lambda x:x**2 if x%2==0 else x**3,l)))


# 3. Filter based on digit properties
# Given:
l = [121, 234, 343, 456, 555, 678, 787]
# Using filter() and lambda, create a new list containing numbers whose first digit and last digit are the same.
# Expected:
# [121, 343, 555, 787]
# Hint: You can convert the number to a string.
print()
print("Output:",list(filter(lambda a:str(a)[0]==str(a)[-1],l)))


# 4. Reduce — difference
# Given:
l = [100, 20, 5, 2]
# Using reduce(), calculate:
# 100 - 20 - 5 - 2
# Expected:
# 73
# Don't use a loop.
# This is a good one because reduce() isn't always about addition or multiplication.
print()
import functools
print("Difference:",functools.reduce(lambda a,b:a-b,l))
print()

# 5. Dictionary comprehension
# Given:
words = ["apple", "banana", "kiwi", "mango"]
# Create a dictionary where:
# - key = word
# - value = number of characters
# Expected:
# {
#     'apple': 5,
#     'banana': 6,
#     'kiwi': 4,
#     'mango': 5
# }
# Use dictionary comprehension.
dic={i:len(i) for i in words}
print(dic)
print()


# 6. Nested loops — multiplication grid
# Print:
# 1  2  3  4  5
# 2  4  6  8 10
# 3  6  9 12 15
# 4  8 12 16 20
# 5 10 15 20 25
for i in range(1,6):
    for j in range(1,6):
        print(f"{i*j:2}",end=" ")
    print()
print()


# 7. Function + string + dictionary
# Define:
# def analyze_string(s):
# The function should return a dictionary containing:
# - number of uppercase letters
# - number of lowercase letters
# - number of digits
# - number of spaces
# For:
s = "Hello Python 123"
# Expected:
# {
#     'uppercase': 2,
#     'lowercase': 10,
#     'digits': 3,
#     'spaces': 2
# }
# Use the string methods you've learned.
def analyze_string(s):
    d={}
    up=0
    lo=0
    digits=0
    space=0
    for i in s:
        if i.isupper():
            up+=1
            d["uppercase"]=up
        elif i.islower():
            lo+=1
            d["Lowercase"]=lo
        elif i.isdigit():
            digits+=1
            d["digits"]=digits
        else:
            space+=1
            d["spaces"]=space
    return d

print("Dict:",analyze_string(s))
print()

# 8. filter() + map() combination
# Given:
l = [12, 15, 22, 31, 40, 53, 60, 71]
# First select numbers that are even and greater than 20.
# Then use map() to replace each selected number with:
# number / 2
# Expected:
# [11.0, 20.0, 30.0]
# The important part is deciding which operation should happen first.
temp=list(filter(lambda x:x>20 and x%2==0,l))
print("Output:",list(map(lambda a:a/2,temp)))
print()


# 9. ⭐ Function + nested loop + condition
# Define:
# def common_elements(l1, l2):
# # Return a new list containing elements that occur in both lists, but don't include duplicates in the result.
# Example:
l1 = [10, 20, 30, 20, 30, 40, 50]
l2 = [30, 50, 60, 30, 70]
# Expected:
# [30, 50]
# Don't use set().
def common_elements(l1,l2):
    new=[]
    for i in l1:
        if i in new:
            continue
        if i in l2:
            new.append(i)
    return new

print("O/P:",common_elements(l1,l2))

# 1. Longest consecutive same-parity sequence ⭐
# Write a function:
# def longest_parity(l):
# Given:
l = [2, 4, 6, 3, 5, 8, 10, 12, 7, 9]
# Find the length of the longest consecutive sequence containing numbers of the same parity.
# Here:
# 2, 4, 6        → 3 even numbers
# 3, 5           → 2 odd numbers
# 8, 10, 12      → 3 even numbers
# 7, 9           → 2 odd numbers
# Expected:
# 3
# Don't use max().
# Topics: function + loop + conditions + variable tracking.
def longest_parity(l):
    even=[]
    odd=[]
    temp=[]
    for i in l:
        if i%2==0:
            temp.append(i)
            even=temp
            l.remove(i)
        else:
            break
