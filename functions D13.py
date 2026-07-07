
a=1,1,2,2,3,3,4,4,
def some(a):
    for j in a:
        print(j)
some(a)

'''
return keyword
--------------
-->in afunction if a return is executed then it will exit from the function
with certain returned values
Example
'''
def myfunc_(a):
    return 5+a
a=myfunc_(10)
b=myfunc_(100)
print(a,b)


import builtins
builtin_functions=[
    name for name in dir(builtins)
    if callable(getattr(builtins,name))]
print(builtin_functions)
print(f"total built-in functions are {len(builtin_functions)}")


'''
                     Recursive Function
                     ------------------
-->Recursive function that calls itself repeatedly until a specified condition is met...

#Syntax
------
def func_name(parameters):
    if condition:-->base case
        return statement
    else:
        return ststement
print(func__name(arguments))
'''

#Example
def func_name(num):
    if num==1:
        return 1
    else:
        return num*func_name(num-1)
num=5
print(func_name(num))

