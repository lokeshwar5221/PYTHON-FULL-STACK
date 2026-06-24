'''
STRING
------
-->String is sequence of char that are enclosed in ' '," ", """ """
-->String is immutable

Concatination
-------------
-->+ operator will work as an addition of two numbers for integers but for rest of the any other like for list,string...etc act as an Concatination...
-->it adds two strings side by side
Example
'''
so="python"
any="is a language"
print(so+any)




'''
INDEXING
--------
-->This is used to access the perticular char in the string by passing the index position value...
-->Indexing start from 0....
-->WE also have negative indexing to count the position from last to first...
EXAMPLE
'''
so="python is a language"
print(so[12])
print(so[-20])




'''
METHODS
-------
1.replace()
----------
-->this method is used to change any substring in that particular string...
syntax-->veriable_name.replace("old_string","new_string")
Example
'''
so="python is a language"
print(so.replace("python","java"))
print(so.replace("a","A"))
print(so.replace("a","A",2))
print(so)

'''
2.join
-------
-->This method is used to add new substring after each char in the string
Example
'''
so="python is a language"
print("#".join(so))

'''
3.split()
--------
-->This method can devide the string into different index into list,based on the string pass by us...
syntax-->variable_name.split('substring')
Example
'''
so="python is a language"
print(so.split(" "))
print(so.split("is"))

'''
4.count()
---------
-->Used to count the substring and perticular string and also specify the index position
-->veriable_name.count("substring",stariting index,ending index)#index is optional
Example
'''
so="python is a language"
print(so.count("a"))

'''
ALL examples of string methods
'''
so="python is a language"
print(so.replace("python","java"))
print(so.replace("a","A"))
print(so.replace("a","A",2))
print(so)
print("#".join(so))
print(so.split("is"))
print(so.count("ia"))




'''
String built-in functions
-------------------------
1.len()
-->This will find the length of the string,which is number of char present in string...
syntax-->len(veriable_name)
Example
'''
so="python is a language"
print(len(so))

'''
2.max()
------
-->we will get the max value in the string
Syntax-->max(veriable_name)
Example
'''
so="python is a language"
print(max(so))

'''
2.min()
------
-->we will get the min value in the string
Syntax-->min(veriable_name)
Example
'''
so="python "
print(min(so))



