'''
self keyword
------------
-->self refers to current object...
'''

class test:
    def display(self):
        print(self)
te=test()
print(te)
te.display()


'''
constructor
-----------
-->This constructor initializes the object automatically when it is created...

'''
#PUBLIC VERIABLES
class batch:
    def __init__(self,name,branch):
        self.name=name
        self.branch=branch
    def display(self):
        print(self.name)
        print(self.branch)
b4=batch('loki','csd')
b4.display()


class fam:
    def __init__(self):
        self._name='loki'
f=fam()
print(f._name)


#PRIVATE VERIABLES

#calling inside the class
class bank:
    def __init__(self):
        self.__pin="2512"
ac=bank()
print(ac._bank__pin)


#calling outside the class
class bank:
    def __init__(self):
        self.__pin='9900'
    def display(self):
        print(self.__pin)
ac=bank()
ac.display()





'''
ENCAPSULATION
-------------




'''
class atm:
    def __init__(self,balance):
        self._balance=balance
    def deposit(self,amount):
        self._balance+=amount
        print(self._balance)
tran=atm(int(input()))
tran.deposit(int(input()))
