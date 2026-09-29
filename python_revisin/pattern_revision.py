# *
# * *
# * * *
# * * * *
# * * * * *
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end=" ")
    print()

print()

# * * * * *
# * * * *
# * * *
# * *
# *
for i in range(5,0,-1):
    for j in range(1,i+1):
        print("*",end=" ")
    print()
print()

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
for i in range(1,6):
    k=1
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
print()


# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
for i in range(1,6):
    for j in range(i):
        print(i,end=" ")
    print()
print()

# 1
# 2 3
# 4 5 6
# 7 8 9 10
# 11 12 13 14 15
k=1
for i in range(1,6):
    for j in range(i):
        print(k,end=" ")
        k+=1
    print()
print()

# A
# A B
# A B C
# A B C D
# A B C D E
for i in range(1,6):
    k=65
    for j in range(i):
        print(chr(k),end=" ")
        k+=1
    print()
print()


# A
# B C
# D E F
# G H I J
# K L M N O
k=65
for i in range(1,6):
    for j in range(i):
        print(chr(k),end=" ")
        k+=1
    print()
print()

# 1
# 1 0
# 1 0 1
# 1 0 1 0
# 1 0 1 0 1
for i in range(1,6):
    for j in range(1,i+1):
        if j%2==0:
            print(0,end=" ")
        else:
            print(1,end=" ")
    print()
print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
k=8
for i in range(1,6):
    for p in range(k):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    k-=2
    print()
print()

# * * * * *
#   * * * *
#     * * *
#       * *
#         *
k=0
for i in range(5,0,-1):
    for p in range(k):
        print(end=" ")
    for j in range(i):
        print("*",end=" ")
    print()
    k+=2
print()


#         *
#       * *
#     * * *
#   * * * *
# * * * * *
#   * * * *
#     * * *
#       * *
#         *
k=8
for i in range(1,6):
    for p in range(k):
        print(end=" ")
    for j in range(i):
        print("*",end="   ")
    print()
    k-=2
#next part
k=2
for i in range(4,0,-1):
    for p in range(k):
        print(end=" ")
    for j in range(i):
        print("*",end="   ")
    print()
    k+=2
print()

# * * * * *
# * * * * *
# * * * * *
# * * * * *
for i in range(1,5):
    for j in range(1,6):
        print("*",end=" ")
    print()
print()


# * * * * *
# *       *
# *       *
# *       *
# * * * * *
for i in range(1,6):
    for j in range(1,6):
        if i==1 or i==5 or j==1 or j==5:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
print()

#         1
#       1   1
#     1   2   1
#   1   3   3   1
# 1   4   6   4   1

s=8
prev=[]
for i in range(0,5):
    for p in range(s):
        print(end=" ")
    current=[]
    for j in range(0,i+1):
        if j==0 or j==i:
            current.append(1)
        else:
            current.append(prev[j-1]+prev[j])
    for j in current:
        print(j,end="   ")
    prev=current
    print()
    s-=2