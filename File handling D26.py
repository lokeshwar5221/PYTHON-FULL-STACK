'''
# File Handling
-------------------
File handler is an object that gives more options like creating, updating.

Two ways to open the file....\
1)open()
----------
Syntax--> do = open('file_name','mode')
          ---------
          -------
          ----
          close()
Example :
'''
do=open('demo.txt','r')
    print(do.read())          

'''
2)with(keyword)

Syntax ---> with open('file_name','mode') as do:

 Modes
-------
'''

# 'r'-->Used to read the file, incase if the file is not present it will raise error.

with open('demo.txt','r') as do:
    print(do.read())




# 'w'-->Used to write the text inside the file..


with open('loki','w') as do:
    print(do.write('We are having SQL class_from 11 am to 1 pm'))




# 'a'--> this is used to add the text at the last position inside the file

with open('demo.txt','a') as do:
    print(do.write('we are using file handling'))


# 'x'-->used to create a new by adding inside the file,incase if the
#    file is present it will raise an error...

with open('roxx.txt','x') as do:
    print(do.write('we are using file handling'))



'''
write()
-------
--> This function is used to add the text inside a file or update a file
with new text...

eg
---
'''
with open('demo.txt','w') as do:
    print(do.write('we are using file handlind'))

with open('demo.txt','a') as do:
    print(do.write('we are using file handlind'))

'''    
read()
------
-->used to read a file and this read()  will read file chunk by chunk
   we can also specify the size

eg
---
'''
with open('demo.txt','r')as do:
    print(do.read())

with open('demo.txt','r')as do:
    print(do.read(10))



'''
readline()
-----------
-->This read line will read a single line at a time...

eg
---
'''
with open('demo.txt','r') as do:
    print(do.readline())



''' 
readlines()
-----------
-->this function will read whole file
'''
with open('demo.txt','r') as do:
    print(do.readlines())
