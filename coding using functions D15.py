
nums=[1,2,3,4,3,2]
empty_=[]
def remove_(nums,empty_):
    for i in nums:
        if i not in empty_:
            empty_.append(i)
    print(empty_)
remove_(nums,empty_)


prime=8
count=0
def prime_not(prime,count):
    for i in range(1,prime+1):
        if prime%i==0:
            count+=1
    if count==2:
        print("prime")
    else:
        print("not prime")
prime_not(prime,count)



char_="loki"
count=0
def length_(char_,count):
    for i in char_:
        count+=1
    print(count)
length_(char_,count)




some="loki is a prohrammer"
count=0
def counting(some,count):
    so=some.split(" ")
    for i in so:
        count+=1
    print(count)
counting(some,count)




so="pytHon Is A prOGraMmINg LanguAge"
upper_=0
lower_=0
space_=0
def count_(so,upper_,lower_,space_):
    for i in so:
        if i.isupper():
            upper_+=1
        elif i.islower():
            lower_+=1
        else:
            space_+=1
    print(f"upper are:{upper_},lower are:{lower_},spaces are:{space_}")
count_(so,upper_,lower_,space_)

