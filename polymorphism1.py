#polymorphism
class A:
    def f(self):
        print("In class A function f")

class B:
    def f(self):
        print("In class B function f")

class C:
    def f(self):
        print("In class C funtion f")

a=A()
a.f()

b=B()                   # same function behaves dicfferently in 3 class
b.f()

c=C()
c.f()