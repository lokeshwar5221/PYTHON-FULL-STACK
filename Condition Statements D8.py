'''
STATEMENTS
----------
1->conditions
   ----------
   1.if
   ->used to check the condition is true or not 
   Example
   '''
num=10
if num%2==0:
    print(f"{num} is an even number")

'''   
   2.if else
   ->else is a fall-back statement incase the if condition is false then the else condition will be executed
   Example
   '''
num=9
if num%2==0:
    print(f"{num} is an even number")
else:
    print(f"{num} is an odd number")

loki_sbi_details={"ATM PIN":"2512"}
pin_=input("enter 4 digit atm pin:")
if pin_ in loki_sbi_details["ATM PIN"]:
    print("welcome to atm")
else:
    print("you entered incorrect pin")

'''    
   3.nested if
   ->if inside the another if is called the nested if
   Example
   '''
loki_sbi_details={"ATM PIN":"2512"}
pin_=input("enter 4 digit atm pin:")
if len(pin_)==4:
    if pin_ in loki_sbi_details["ATM PIN"]:
        print("welcome to atm")
    else:
        print("you entered wrong pin")
else:
    print("plese enter 4 digit pin")


