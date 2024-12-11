def isprime(n):
    if n==1:
        return False
    is_prime = True
    for i in range(2,n):
        if n%i==0:
            is_prime = False
            break
    return is_prime 
a = int(input())
b = int(input())
print(f"Prime Numbers from {a} to {b} ")
count = 0
for n in range(a,b+1):
    if isprime(n):
        print(n)
        count = count+1
print("count : ",count)