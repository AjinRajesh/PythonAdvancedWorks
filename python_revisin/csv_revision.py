f=open("stu_data.csv","w+",newline="")
cont=[
    ["Name","Mark"],
    ["Ajin",100],
    ["Arun",62],
    ["Anu",87],
    ["John",90]
]
import csv
w=csv.writer(f)
print(w)
w.writerows(cont)
print(w)
f.seek(0)
r=csv.reader(f)
next(r)
for i in r:
    if int(i[1])>70:
        print(i[0], i[1])
f.close()