'''
Inheritance
-----------
-->Inheritance is an oop concept where one class (child/derived) acquired the properties
and methods of another class(parent/base)

class parent:
    pass
child class(parent):
    pass

1.single inheritance
--------------------
A child class inherits from one parent is single inheritance
'''

class animal:
    def sound(self):
        print("animal makes sound")
class dog(animal):
    def bark(self):
        print("dog barks")
s=dog()
s.sound()
s.bark()

class father:
    def land(self):
        print("5 acer of land")
class son(father):
    def flat(self):
        print("3BHK Flat")
so=son()
so.land()
so.flat()


'''
2.multiple inheritance
-------------------
a child inherits maore than  one parent is called multiple inheritance
'''
class father:
    def skills(self):
        print("driving")
class mother:
    def talent(self):
        print("cooking")
class sister:
    def learn(self):
        print("time pass")
class son(father,mother,sister):
    def mine(self):
        print("coding")
so=son()
so.skills()
so.talent()
so.learn()
so.mine()


'''
3.Multi-level
-------------
child class will act as an parent class for another class

'''
class grandfather:
    def house(self):
        print("have a house")
class father(grandfather):
    def flat(self):
        print("have a flat")
class son(father):
    def car(self):
        print("have a car")
so=son()
so.house()
so.flat()
so.car()


'''
4.Hierarchical
--------------
-->multiple childs inherits from the same parent

'''
class mother:
    def gold(self):
        print("10 kg gold")
class priya(mother):
    def some(self):
        print("5kg golg")
class padma(mother):
    def some1(self):
        print("remaining 5kg gold")
so_=priya()
so_1=padma()

so_.gold()
so_.some()

so_1.gold()
so_1.some1()


'''
5.Hybrid inheritance
--------------------
-->This is the combination of two or more types of inheritance
example of multiple + multi-level

'''

class a:
    def methoda(self):
        print("class a")
class b(a):
    def methodb(self):
        print("class b")
class c(a):
    def methodc(self):
        print("class c")
class d(b,c):
    def methodd(self):
        print("class d")
class e(c):
    def methode(self):
        print("class e")
so=d()
so.methoda()
so.methodb()
so.methodc()
so.methodd()
ac=e()
ac.methoda()
ac.methodc()
ac.methode()


'''
super()
-------
-->this super function is used to access the parent class method or constructor in
the child class...

'''
class parent:
    def show(self):
        print("parent method")
class child(parent):
    def show(self):
        super().show()
        print("child class")
so=child()
so.show()


#using constructor
class person:
    def __init__(self,name):
        self.name=name
class student(person):
    def __init__(self,name,roll):
        super().__init__(name)
        self.roll=roll
    def display(self):
        print(self.name)
        print(self.roll)
so=student("loki","234")
so.display()
        









