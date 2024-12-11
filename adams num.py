org =input()
j =len(org)
n = org
rev = 0
for i in range(j):
    n = int(n)
    d = n%10
    n = n//10
    rev  = rev*10 +d
sq_rev = rev**2
org = int(org) 
sq_org =org**2
x = sq_org
sq_org_rev = 0
for i in range(j+1):
    s = x%10
    x =  x//10
    sq_org_rev = sq_org_rev*10 + s
if sq_rev==sq_org_rev:
    print("adams number")
else:
    print("not an adams number")