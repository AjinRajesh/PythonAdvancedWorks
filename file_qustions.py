# # #write a program to read a text file and displays the number of lines in a file
from gettext import find

# f=open('k.txt','r')
# s=f.readlines()
# print("No of lines:",len(s))
#
# # # #write a program to display the number of words in a file
# f.seek(0)
# s=f.read()
# count=0
# for i in s.split():
#     count+=1
# print("No of words:",count)
#
# # # #write a program to update the second line in a file
# f.seek(0)
# s=f.readlines()
# s[1]="Ajin\n"
# f.close()


# g=open('k.txt','w')
# g.writelines(s)
# print("After updating:",s)
# g.close()


# # #write a program to display the last 5 lines in a file
# print("Last five line:",s[-5:])

#
# #program to search a particular word in a file
# f=open('k.txt','r')
# wrd=input("Enter word to search:")
# s=f.read()
# if wrd in s:
#     print("Found")
# else:
#     print("not found")
# f.close()

#
# #find the number of letters,digits,and spaces in a file
# f=open('k.txt','r')
# letters=0
# digits=0
# spaces=0
# s=f.read()
# for i in s:
#     if i.isalpha():
#         letters+=1
#     elif i.isdigit():
#         digits+=1
#     elif i.isspace():
#         spaces+=1
# print(f"Number of letters = {letters}")
# print(f"Number of digits = {digits}")
# print(f"Number of spaces = {spaces}")


#reverse the lines in a file
# f.seek(0)
# s=f.readlines()
# for i in s:
#     print(i[::-1],end=" ")
#
# f.close()

# A file totalstudents.txt contains the names of all students in a class,
f=open('totalstudents.txt','w')
f.writelines(['Ajin\n','john\n','Arunima\n','Lekshmi\n','Aneeta\n'])
# and a file passedstudents.txt contains the names of students who passed.txt the exam.
g=open('passedstudents.txt','w')
g.writelines(['Ajin\n','john\n','Aneeta\n'])
# Write a Python program to:
# Read the names from both files.
f.close()
g.close()
f=open('totalstudents.txt','r')
g=open('passedstudents.txt','r')
print("Total students:")
print(f.read())

print("Passed students:")
print(g.read())

# # Find the students who did not pass.
# # Write their names to a new file named failed_students.txt, one name per line.
# #
f.seek(0)
g.seek(0)
h=open('failedstudents.txt','w')
s=f.readlines()
y=g.readlines()
for i in s:
        if i not in y:
            print(f"{i.strip()} did not pass")
            h.write(i)
        else:
            continue
