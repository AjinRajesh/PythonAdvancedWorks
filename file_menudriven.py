def file_read():
    file_name=input("Enter the file name: ")
    f=open(file_name,"r")
    f.seek(0)
    print("File Content:")
    print(f.read())
    f.close()

def file_write():
    file_name=input("Enter file name: ")
    f=open(file_name,"w")
    while True:
        content=input("Enter the content(Enter 'done' when finished): ")
        if content=="done":
            break
        f.write(content+"\n")
    f.close()

def file_append():
    file_name=input("Enter the file name: ")
    f=open(file_name,"a")
    while True:
        content = input("Enter the content(Enter 'done' when finished): ")
        if content == "done":
            break
        f.write(content + "\n")
    f.close()

def file_search():
    file_name=input("Enter the file name: ")
    f=open(file_name,"r")
    word=input("Enter the word to search: ")
    content=f.read()
    if word in content:
        print(f"{word} found in {file_name}")
    else:
        print(f"{word} not in {file_name}")
    f.close()

def file_delete():
    file_name=input("Enter the file name: ")
    import os
    os.remove(file_name)


while True:
    ch=int(input("1.File Read\n2.File Write\n3.File Append\n4.File Search\n5.File Delete\n6.Exit\nEnter Your Choice: "))
    if ch==1:
        file_read()
    elif ch==2:
        file_write()
    elif ch==3:
        file_append()
    elif ch==4:
        file_search()
    elif ch==5:
        file_delete()
    elif ch==6:
        exit()
    else:
        print("Invalid Operation!!")
        print()
        continue
    print()
