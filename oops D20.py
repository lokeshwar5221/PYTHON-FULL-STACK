'''
use
---
-code reusable
-easy maintance
-clear understanding
-better security

Classes
-------
class is a blue print or a templete used to create an object...

class batch_4:
    pass



Object
------
-object is a instance of class
'''
class student:
    stu='loki'
st_=student()
print(st_)

'''
Attributes
----------
->Attributes are the variable that belongs to an object or the class
'''
class how:
    def details(self,name,age):
        self.name=name
        self.age=age
##    def nam(self):
##        print(self.name)
s1=how()
s1.details('loki',21)
print(s1)

'''
Methods
-------
-->methods are nothing but,the function inside the class
'''
class calculator:
    def add(self,num,num2):
        print(num+num2)
    def sub(self,num,num2):
        print(num-num2)
cal=calculator()
cal.add(2,4)
cal.sub(6,7)

