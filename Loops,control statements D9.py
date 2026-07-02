'''
                                LOOPS
                                -----
1.for loop
-->a for loop is used to itterate over a sequence ,list,tuple
Example
'''
any_="python is a language"
for j in any_:#j is called the instance veriable
    print(j)

any_=[1,2,3,4,5]
for any_2 in any_:#j is called the instance veriable
    print(any_2)
    
any_={"name":"loki",
      "role":"student"}
for j in any_.keys():
    print(j)

any_={"name":"loki",
      "role":"student"}
for j in any_.values():
    print(j)

'''
else in for loop
----------------
-->the else block will be executed after the for loop
'''
any_=(1,2,3,4,5)
for j in any_:
    print(j)
else:
    print("program is ended")

'''
range
-----
-->range is a inbuilt function that is used to generate a sequence upto a limit
syntax->range(start,end,step)
Example
'''
all_=(1,2,3,4,5,6)
for j in range(1,50):
    print(j)

all_=(1,2,3,4,5,6)
for j in range(1,50,2):
    print(j)



'''    
2.while loop
-->will execute until the condition becomes true...
Example
'''
i=1
while i<5:
    print(i)

i=1
while i<5:
    print(i)
    i+=1


'''
                      control statements
                      ------------------
1.break
-->it is usedv to exit from the loop
Example
'''
any_=(1,2,3,4,5)
for j in any_:
    print(j)
    if j==3:
     break
else:
    print("entered")

'''
2.continue
----------
-->it will skip the current itteration 
Example
'''
any_=(1,2,3,4,5,6)
for j in any_:
    if j==3:
        continue
    print(j)
else:
    print("entered")

'''
3.pass
------
-->space holder
Example
'''
any_=(1,2,3,4,5)
for j in any_:
    pass



'''
assert keyword
--------------
-->it will used to check the condition but it will raise an error incase it is false...
Example
'''
age=int(input("entrer your age:"))
assert age>=18,"your must have 18 years"
print("you are elegible")
