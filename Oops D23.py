'''
Polymorphism
------------
-->polymorphism means many forms
-->it allows same method,function or operator to perform different
tasks depending on the same object...

Types
-----
1.Method Overloading
--------------------
-->Method Overloading means having multiple methods with the same name
but different parameters
-->recent method near to the object will be executed

'''
class cal:
    def add(self,num,num2=0):
        print(num+num2)
    def add(self,num,num2=0,num3=7):
        print(num+num2+num3)
so=cal()
so.add(1,5)
so.add(2,3,5)

'''
2.Method Overriding
-->The method overriding occurs when a child class provides its own
implementation of a method already defined in its parent class... 

'''
class animal:
    def sound(self):
        print("animals makes sound")
class dog(animal):
    def sound(self):
        print("dog barks")
so=dog()
so.sound()
'''
3.Operator Overloading
----------------------
-->This allows operators (+,-,*) to work differently for user_defined object

1.__add__(+)
2.__sub__(-)
3.__mul__(*)
4.__truediv__(/)
5.__eg__() (==)
6.
'''
class student:
    def __init__(self,marks):
        self.marks=marks
    def __sub__(self,other):
        return self.marks+other.marks
s1=student(3)
s2=student(4)
print(s1-s2)



'''
Data Abstraction
----------------
-->Data Abstraction is the process of hiding implementation details and
showing only the essential data to the user

Eg
---
-ATM
-CAR
-APP


from abc import ABC,abstractmethod
class parent:
    @abstractmethod
    def display(self):
        pass
'''

from abc import ABC,abstractmethod
class bank:
    @abstractmethod
    def interest(self):
        raise NotImplementedError('sub class must implement interest()')
class SBI(bank):
    def interest(self):
        print('SBI interest rate:6.5%')
class HDFC(bank):
    def interest(self):
        print('HDFC interest rate: 5.5%')
class ICICI(bank):
    def interest(self):
        print('ICICI interest rate: 6.9')
banks=[SBI(),HDFC(),ICICI()]
for j in banks:
    j.interest()
    
