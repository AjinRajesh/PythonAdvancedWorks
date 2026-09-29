#--------------WRITE
# import csv
# f=open("sample.csv","w",newline="")
# content=[
# ['name','age','place'],
# ['arun',22,'ekm'],
# ['amal',23,'kgd']
# ]
#
# #w=csv.writer(filereference)
#
# w=csv.writer(f)#writer object is created
# print(w)
# w.writerows(content)#writes each row to
# f.close()


#-----------READ
import csv
f=open("sample.csv","r")
r=csv.reader(f)
print(r)
for i in r:
    #print(i)#print each row
    #print(i[0])#print first column
    print(i[1])#print 2nd column
f.close()