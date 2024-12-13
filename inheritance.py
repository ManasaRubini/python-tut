class A:
    a = 10
class C:
    c = 30
class B(A,C):
    b = 20
obj = B()
print(obj.c)