'''
LIST DATA TYPES
---------------
-->List is a collection of different datatypes that are enclosed in [] sepetrsted by commas ,
-->List is mutable

MUITABLE                                        IMMUTABLE
--------                                        ---------
The datatypes can be modified                   Cant be modified
ex-->any_=[1,2,3,4]                             ex-->so="python is a language"
     print(any_)                                          print(so.replace('python',java))
     any_.append(5)                                       print(so)   
     print(any_)
     any_.append(10)
     print(any_)                                  



                                                     
Methods
-------
1.append()  
----------
-->it will add the given value to the list at the last index position
Example
'''
any_=[1,2,3,4]
print(any_)
any_.append(5)
print(any_)
any_.append(10)
print(any_)
any_.append('python')
print(any_)

'''
2.extend()
----------
-->This is also add a item in the last index position,but it will give each value seperately
Example
'''
any_=[1,2,3,4]
any_.extend('python')
print(any_)

'''
3.pop()
-------
-->used to delete the valus from the list but it will delete based on the index position
Syntax-->veriable_name.pop(index position)
Example
'''
any_=[1,2,3,45,67,89]
any_.pop(5)
print(any_)

'''
4.remove()
----------
-->used to delete the item from the list,but it will del the value fronm the list
Syntax-->veriable_name.remove(value)
Example
'''
any_=[1,2,3,45,67,89]
any_.remove(67)
print(any_)


any_=[1,2,'python is a language',[45,78,"java is a language",[1,23],90],'hello']
print(any_[3][2][10])
print(any_[3][3][1])



'''
TUPLE
-----
-->List is a collection of different datatypes that are enclosed in () sepetrsted by commas ,
-->It is immutable

METHODS
-------
1.index()
--------
-->used to find the index position of perticular value in the tuple
Example
'''
how=(1,2,3,4,'python',[4,5],(90,78))
print(how.index("python"))

'''
2.count()
--------
'''
how=(1,2,3,4,'python',[4,5],(90,78))
print(how[5][1])
print(len(how))
print(how.index("python"))
print(how.count('python'))
#any_=[56,[1,2],['python','java',['python is a language',153,90],[78,6],'i knowc']]
#count,index(know
