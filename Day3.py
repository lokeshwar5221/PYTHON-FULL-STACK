'''
Python project -> POP/OOP --> DSA (Logic based-> pattern based ->platform
POP (Procedure Oriented Programming) --> Dividing the entire code into
blocks -> procedures->functions (def)
Functions -> A reusable block of code (A block of statements which performs
a specific task)

Syntax:
def <funcname>(parameters):
    """Doc string"""
    statements(s)...
    ..........
    ..........(body of the function)
    return values(s)....
fname(args)#func call

#simple senario to understand
def add(a,b):
    """adition function"""
    c=a+b
    return c
print(add(5,6))

def sample(*a):
    print(a)
    print(type(a))
sample()
sample(1,2,3,4,5)
sample('codegnan',[25,12],'poll',2+5j)
marks=[20,14,56,78]
sample(marks)
sample(*marks)
# * used to unpack the values into a collection
a,*b,c=23,4,'loki',[23,45],'sai',90
print(a)
print(b)
print(c)


def add(*a):
    """perform addition for numeric values"""
    print(a)
    result=0
    for i in a:
        if type(i) in [int,float,list]:
            result=result+i
    return result
print(add(13,'loki',7,5))


#keyword argument-->we can pass the name for the arguments
def batch(name,age,place='vizag'):
    """keyword argument usage"""
    print(f'{name} lives in {place} and age was {age}')
batch('loki',24,'guntur')
batch(place='hyd',name='sai',age='21')
#keyword argument only need name matching not order
batch(name='roxx',age=20)
#default argument can accept a value as default

print(4,5)
print(4,5,sep=':')#Here keyword argument is sep and we are changing
#the default value for sep


#keyword variable length rguments(**kwargs)-->anu number of
#keyword argument,data is stored in dictionary

def batch(**a):
    print(a)
    print(type(a))
batch()
batch(name='loki',age=21,place='vizag',brance='csd')
data={'name':['loki','sai'],'place':['vizag','rjy']}
batch(**data)
'''

def student_details_marks(*marks,**details):
    print(details)
    total=0
    avg=0
    for i in marks:
        total+=i
    avg=total/len(marks)
    print(total,avg)
details={'name':'loki','age':21,'place':'vizag','brance':'csd'}
marks=(45,56,88,98,88,74)
student_details_marks(**details,*marks)
