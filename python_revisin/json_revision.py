# f = open("student.json","w")
# import json
# student={
#     "name":"Ajin",
#     "age":23,
#     "course":"Python"
# }
# json.dump(student,f)
# f.close()
#
# f=open("student.json","r")
# cont=json.load(f)
# print(cont)
# f.close()

#---------List of dictionaries--------------
# f=open("students.json","w+")
# import json
# student=[
#     {"name":"Ajin","mark":100},
#     {"name":"Anu","mark":95},
#     {"name":"Luffy","mark":55}
# ]
# json.dump(student,f)
# f.seek(0)
# cont=json.load(f)
# for i in range(len(cont)):
#     print(f"{cont[i]['name']} : {cont[i]['mark']}")
# f.close()


#---JSON modify data-----------
f=open("products.json","w+")
import json
products = [
    {"name": "Laptop", "price": 50000},
    {"name": "Phone", "price": 20000},
    {"name": "Watch", "price": 3000}
]
json.dump(products,f)
f.seek(0)
cont=json.load(f)
print(cont)
cont[0]["price"]=55000
cont.append({"name":"Tablet","price":25000})
print(cont)
f.seek(0)
json.dump(cont,f)
f.close()