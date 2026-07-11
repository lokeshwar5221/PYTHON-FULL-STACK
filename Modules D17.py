'''
                        Modules
                        -------
-->A module is a python file(.py) that contains reusable code

1.variables
2.functions
3.classes
4.objects
5.statements

why this
--------
-->Instead of writing the same code repetedly,we can store it in a module
and use it whenever needed...

Types of modules
----------------
1.user-defined
2.Built-in

1.user-define
-------------
'''
#1.user-defined
import calculator
print(calculator.add(1,2))


#import specific function
from calculator import add,sub
print(sub(4,2))

from calculator import *
print(div(4,2))

#import as allis name
import calculator as m
print(m.mul(3,4))
print(m.pow(2,3))


'''
2.Built-in
----------
->math
->os
->sys
->random


math
----
-->this module is used to do mathematical operations

sqrt()        -->square root
factorial()   -->factorial
pow()         -->power
ceil()        -->round up
floor()       -->round down
'''
import math
print(math.pow(1,2))
print(math.sqrt(25))
print(math.factorial(5))




'''
os
--
-->The os module is used to interact with operating system

-sys
-random
'''

import os
print(os.getcwd())#current directory
os.mkdir("lokiroxx")#create new folder
os.rmdir("lokiroxx")#remove existing folder


'''
sys
---
-->this will provide the information about python interpeter
'''
import sys
print(sys.version)


'''
random
------
-->used to generate random value
'''
import random
print(random.randint(1000,9999))

colour=['red','yellow','blue','green']
print(random.choice(colour))
