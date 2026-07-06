'''
                   FUNCTIONS
                   ---------
-->Functions is a block of code that can be reusable
-->Function can avoid the repeated line of code...

Functions are of 2 types
------------------------
1.built-in
----------
eg->print(),max(),min(),sum(),type()

2.user-defined
--------------
-->this function starts with a key wordb (def)

def func_name(parameters):
    ----------
    --------
    ------
func_name(arguments)

Example
'''
def add(a,b):
    print(a+b)
add(4,5)

def add():
    print("hello")
add()


'''
types of arguments
------------------
1.Required arguments
--------------------
-->They have to pass same number of arguments with desination of the fumnction...
Example
'''
def add(a,b):
    print(a+b)
add(3,1)#you have too pass the same no of arguments

    
'''
2.Default arguments
-------------------
Example
'''
num=7
num_2=9
num_3=8
def add(a,b,c):#parameters
    print(a)
    print(b)
    print(c)
add(num,num_2,num_3)#arguments
    
'''
3.Keyword
->we can pass a pairb like veriable=datatype
4.variable length
-----------------
-->can pass n number of arguments and just use args in the parameters,will receive tuple os arguments throught indexing
Example
'''
#(*args)
num=7
num_2=9
num_3=8
num_4='loki'
def add(*a):
    print(a)
add(num,num_2,num_3,num_4)

#(**) they take the data in the form of dictionary
def add(**sum):
    print(sum['age'])
add(name='loki',age=21)


#Global veriable and local veriable
num=89#Global veriable can be accessed at any part in the program
def fun_():
    num=9#local veriable cannot be accessed out side of the function
    print(num)
fun_()

#changeing the values of global veriable value by using keyword (global) that can be changed completely inside and outside of the function
num=9
def fun_():
    global num
    num=89
    print(num)
fun_()
print(num)
