
#----------------WRITE---------------
# import json
# f=open("sample.json","w")
# content=[
#         {"name":"ajin","age":23},
#         {"name":"amal","age":22}
#         ]
# json.dump(content,f)
# f.close()

#---------------READ-------------
import json
f=open("sample.json","r")
content=json.load(f)
print(content)
print(content[0])
print(content[0]["name"])
f.close()