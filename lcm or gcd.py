a = int(input())
b = int(input())
i = max(a,b)
while True:
    if i%a==0 and i%b==0:
        print("lcm:",i)
        break
    i = i+1
