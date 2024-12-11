def calc(a,b):
    return a+b,a-b

x,z = calc(5,2)
t = x,z
print(x,z)
for z in t:
    print(z)