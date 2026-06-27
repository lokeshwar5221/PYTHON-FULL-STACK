'''
DICTIONARY
----------
-->dict is a key:value pair seperated by:,and keys are unique
-->the place of keys we have to use immutable data types...
-->dict is muitable

Example
'''
details_={'name':'loki',
          1:'number',
          (4,5):[2,4]}
print(details_)



'''
METHODS
-------
1.keys()
--------
-->used to get all the keys from the dictionary
syntax-->variable_name.keys()
Example
'''
details_={"name":"loki",
         "age": 21,
         "gender":"male"}
print(details_.keys())


'''
2.values
--------
-->used to get all the values from the dictionary
Example
'''
details_={"name":"loki",
         "age": 21,
         "gender":"male"}
print(details_.values())


'''
3.items()
--------
-->used to get all the items from the dictionary
Example
'''
details_={"name":"loki",
         "age": 21,
         "gender":"male"}
print(details_.items())
print(details_['age'])


'''
4.clear()
--------
-->if we use this the entire dictionary will be cleared
Example
'''
details_={"name":"loki",
         "age": 21,
         "gender":"male"}
details_.clear()
print(details_)


'''
5.update()
----------
-->by using this we can update any value in the dictionary
Example
'''
details_={"name":"loki",
         "age": 21,
         "gender":"male"}
details_.update({'name':'sai'})
details_.update({'ph':445565})
print(details_)






'''
SETS
----
-->sets are collection of un ordered elements that are seperated by ,
-->set is muttable
-->can remove duplicate value by itself...
Example
'''
go={1,2,3,4,5,6,7}
print(go)

'''
METHODS
-------
1.union()(|)
-->combines the elements from both sets
syntax-->set_1.union(set_2)
Example
'''
go={1,2,4,6,7,8}
so={89,76,55,77}
print(go|so)
print(go.union(so))

'''
2.intersection()
----------------
-->common elements from the both sets
syntax-->set_1.intersection(set_2)
Example
'''
go={1,2,4,6,7,8}
so={4,5,8,89,76,55,77}
print(go&so)
print(go.intersection(so))

'''
3.symmetric_difference()
-----------------------
-->all different elements fron both sets
syntax-->set_1.symmetric_difference(set_2)
Example
'''
go={1,2,4,6,7,8}
so={4,5,8,89,76,55,77}
print(go^so)
print(go.symmetric_difference(so))

go={44,10,2,3,4,5,6}
go.add(90)
#go.pop()
#go.remove(4)
#go.discard(9)
print(go)
