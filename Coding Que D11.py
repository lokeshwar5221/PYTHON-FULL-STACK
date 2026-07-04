'''
#1.palindrome
so=input("enter a word:")
empty=""
for i in so:
    empty=i+empty
if empty==so:
    print(f"{so} is a palindrom")
else:
    print(f"{so} is not a palindrom")

#2.Fibonacci
num=0
num1=1
limit=int(input("enter limit:"))
print(num,num1,end=" ")
for i in range(1,limit+1):
    all=num+num1
    num=num1
    num1=all
    print(all,end=" ")

#3.Calculator
num=int(input("enter"))
num1=int(input("enter"))
opp=int(input("enter \n1.add \n2.sub \n3.mul \n4.pow \n5.div \nenter your option"))
if opp==1:
    print(num+num1)
if opp==2:
    print(num-num1)
if opp==3:
    print(num*num1)
if opp==4:
    print(num**num1)
if opp==5:
    print(num/num1)
    
#4.Multiplication table
table=int(input("enter table number:"))
limit=int(input("enter range:"))
for i in range(1,limit+1):
    print(f"{table} x {i} = {table*i}")
'''

num=int(input("enter number"))
sum_=0
for i in range(1,num):
    if num%i==0:
        sum_+=i
if num==sum_:
    print(f"{num} is perfect")
else:
    print(f"{num} is not")
    

