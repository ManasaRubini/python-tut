n = 3
for i in  range(n):
    for j in range (n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if i+j>=n-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(n):
        if i>=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
a = 6
for i in range(a):
    for j in range (a):
        if i<=j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    for j in range(a):
        if i+j<=a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()
    