n = input()
r = len(n)
print(r)
print("first char:",n[0])
print("second char:",n[-1])
print("Upper case:",n.upper())
print("Lowercase:",n.lower())
substring = n[r//2:-1]
print("substring:",substring)
