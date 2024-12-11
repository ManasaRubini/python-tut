n = 10
for i in range(n):
    for j in range(n):
        if i==n-2 and j==n-6 or i==n-4 and j==n-8 or i==n-6 and j==n-n or i==n-8 and j==n-n or i==n-n and j==n-8 or i==n-8 and j==n-6 or i==n-n and j==n-4 or i==n-8 and j==n-2 or i==n-6 and j==n-2 or i==n-4 and j==n-4:
             print("*",end=" ")
        else:
            print(" ",end=" ")     
    print()