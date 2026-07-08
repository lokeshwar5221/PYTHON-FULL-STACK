'''
                    LAMBDA FUNCTION
                    --------------
-->This is alse as annonymous function...
-->a lambda function can take n number of arguments but only one expression...

syntax-->lambda argument:expression
Example
'''
some=lambda a,y,b:a+y+b*2
print(some(10,2,4))
'''
filter()
--------
-->this is a built in function used to filter elements from an itterables such
as list,tuple,and set basedon condition

syntax-->filter(function,itterable)

-->this filter() function returns filter object so we can convert that into
list,set and tuple
'''
nums=[1,2,3,4,5]
rev=filter(lambda a:a%2==0,nums)
print(list(rev))

nums=[1,2,3,4,5]
rev=filter(lambda a:a%2!=0,nums)
print(set(rev))

'''
                  List comprehension
                  ------------------
-->this offers a shorter when we want to create a new list from
the old

syntax-->variable_name=[expression loop condition]
'''
#without condition
old=[1,2,3,4,5,5,6,6]
new_=[i for i in old]
print(new_)


#with condition
old=[1,2,3,4,5,5,6,6]
new_=[i for i in old if i%2==0]
print(new_)

'''
                dictionary comprehension
                ------------------------
-->This offer a shorter syntax when we want to create a new dict from the old dict
syntax-->veriable_name=[exprexxion loop]

'''
#with condition
old_dict={1:2,3:7,5:6}
new_dict={i:j for (i,j) in old_dict.items()}
print(new_dict)


#without condition
old_dict={1:2,3:7,5:6}
new_dict={i:j for (i,j) in old_dict.items() if j%2==0}
print(new_dict)
