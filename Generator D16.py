'''
                        GENERATORS
                        ----------
-->this generate a special function that returns the itertor,instead of
returning all the values at once...
-->here we are going to use yield keyword
'''
def some():
    yield 1
    yield 2
    yield 3
so=some()
print(next(so))
print(next(so))
print(next(so))

'''
Working of Generator
--------------------
-->when a function is called
-->it does not execute the function immediately...
-->it will returns the generator objectn
-->then the function will pause at each yield...
-->When the next() is called again,execution resumes from where it stopped

'''
def demo():
    print("start")
    yield 1

    print("middle")
    yield 2

    print("end")
    yield 3
how=demo()
print(next(how))
print(next(how))
print(next(how))




def how(so):
    for i in range(so):
        yield i*i
any_=how(50)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))

def how(so):
    for i in range(so):
        print(i*i)
how(4)



'''
functions                              Generator
--------                               ---------
->return                               ->yield
->return complete result               ->return one value an once
->function will end after the return   ->pass after every yield
  the values
->more memory usage                    ->less meomory usage
->This function never resume           ->resume after next()


yield keyword
-------------
-->This will produce the value
-->But the Yield pause the function
-->and yield will save the function current status
-->yield will continue where it stoped...


next() keyword
--------------
-->The next() function is used to retrive the next value from a generator
example
'''

def how(so):
    for i in range(so):
        yield i*i
any_=how(50)
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))
print(next(any_))


'''
stopitteration
--------------
-->Calling next function after all values retrived then it will raise the
stopItteration exception

'''
def loop(a):
    for i in range(1,a+1):
        for j in range(1,a+1):
            print(i*j)
            yield 1
so=loop(5)
print(next(so))
