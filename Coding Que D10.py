1.Prime Number

num=int(input("Enter a Number:"))
count=0
for j in range(1,num+1):
    if num%j==0:
        count+=1
if(count==2):
    print(f"{num} is a prime number")
else:
    print(f"{num} is a not prime number")


2.Generate the prime number to certain range

limit_=int(input("enter a number:"))
for j in range(1,limit_+1):
    count=0
    for i in range(1,j+1):
        if j%i==0:
            count+=1
    if count==2:
        print(f"{j} is a prime number")


3.print pattern(Right angle Triangle) using stars
*
**
***
****
*****

num=5
for j in range(1,num+1):
    for i in range(1,j+1):
        print("*",end=" ")
    print()   


4.print pattern(Right angle Triangle) using numbers
1
1 2
1 2 3
1 2 3 4
1 2 3 4 5

num=int(input("Enter a Number:"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(i,end=" ")
    print()    


5.print pattern(Right angle Triangle) using numbers
1
2 2
3 3 3
4 4 4 4
5 5 5 5 5

num=int(input("Enter a Number:"))
for j in range(1,num+1):
    for i in range(1,j+1):
        print(j,end=" ")
    print()    


6.print pattern(Right angle Triangle) using numbers
1
2 3
4 5 6
7 8 9 10

num=int(input("Enter a Number:"))
count=0
for j in range(1,num+1):
    for i in range(1,j+1):
        count+=1
        print(count,end=" ")
    print()


7.print pattern(Right angle Triangle) using numbers reverse
1 2 3 4 
5 6 7 
8 9 
10 

num=int(input("Enter a Number:"))
count=0
for j in range(num,0,-1):
    for i in range(1,j+1):
        count+=1
        print(count,end=" ")
    print()


8.print pattern(Right angle Triangle) using stars
* * * * * 
* * * * 
* * * 
* * 
* 

num=5
for j in range(num,0,-1):
    for i in range(1,j+1):
        print("*",end=" ")
    print()


9.check the number is armstrong or not

am_str=int(input("Enter a number:"))
length_=len(str(am_str))
all_sum=0
for j in str(am_str):
    all_sum+=int(j)**length_
if all_sum==am_str:
    print(f"{am_str} is a amstrong number")
else:
    print(f"{am_str} is a amstrong number")


10.check the number is prefect or not

prefect_=int(input("Enter a Number:"))
all_sum=0
for j in range(1,prefect_):
    if prefect_%j==0:
        all_sum+=j
if all_sum==prefect_:
    print(f"{prefect_} is a prefect number")
else:
    print(f"{prefect_} is a not prefect number")

11.print a pyramid using stars
          *
         ***
        *****
       *******
      *********
     ***********
    *************
   ***************
  *****************
 *******************

num=int(input("Enter a Number:"))
for j in range(num):
    print(" "*(num-j-1),end=" ")
    print("*"*(2*j+1))

11.print a reverse right angle using numbers
 1  2  3  4  5 
 1  2  3  4 
 1  2  3 
 1  2 
 1 

num=5
for j in range(num,0,-1):
    for i in range(1,j+1):
        print("",i,end=" ")
    print()

12.print 
*  *  *  *  * 
*  *  *  * 
*  *  *
*  * 
*
num=5
for j in range(num,0,-1):
    for i in range(1,j+1):
        print("","*",end=" ")
    print()

13.print a triagnle  using characters
a 
b c 
d e f 
g h i j 
k l m n o

n=5
ch=97
for j in range(1,n+1):
    for i in range(j):
        print(chr(ch),end=" ")
        ch+=1
    print()

14.print 
a b c d e 
f g h i 
j k l 
m n 
o 

n=5
ch=97
for j in range(n,0,-1):
    for i in range(j):
        print(chr(ch),end=" ")
        ch+=1
    print()   

15.print
     A
    BBB
   CCCCC
  DDDDDDD
 EEEEEEEEE

num=5
ch=65
for j in range(num):
    print(" "*(num-j-1),end=" ")
    print(chr(ch)*(2*j+1))
    ch+=1
    
16.print
    1
   234
  56789

num=3
count=1
for j in range(1,num+1):
    print(" "*(num-j),end="")
    for i in range(2*j-1):
        print(count,end="")
        count+=1
    print()
'''



    
rows=5
for j in range(rows) :
    for i in range(j):
        print(" ",end=" ")
        for k in range(rows-i):
            print("*",end=" ")
    print()
'''
    
