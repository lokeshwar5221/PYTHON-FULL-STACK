'''
Moduel--> A Module is simple python file or block of code(reusable,organized code)
import keyword

orgenization-->Class

Encapsulation,inheritance,Polymorphism
employee--->function
'''

def employee(*names,**settings):
    """employee details along with their settings"""
    for employee in  names:
        print("-----------")
        print('-',employee)
    for key,value in settings.items():
        print('key is',key)
        print("value is",value)
##employee("loki","sailu","roxx",department="operations",
##         experience_letter=True,salary=True)
details={'orgenization':'codegnan',
         'year':2018,
         'branches':['vizag','hyd','vijayawada']}
print(__name__)
