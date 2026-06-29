'''
Type Convertions
----------------
This is a proicess of converting one data type to another data type...

int : string float
Example
'''
num=89
num2=float(num)
print(num2)
print(type(num))
so=str(num)
print(so)


'''
float : string;integer
Example
'''
num=89
num2=float(num)
print(num2)
print(type(num))
so=str(num)
print(so)


'''
string : integer;float;list;tuple
Example
'''
hai='789'
num=int(hai)
print(num)

hello_='67.98'
num2=float(hello_)
print(num2)
print(num+num2)

any_="python"
con_=list(any_)
print(con_)
any_2='123456'
con_2=list(any_2)
print(con_2)

any_="python"
con_=tuple(any_)
print(con_)
any_2='123456'
con_2=tuple(any_2)
print(con_2)



'''
list : string;tuple;dictionary
Example
'''
var_=['p','y','t','h','o','n']
text_=''.join(var_)
print(text_)

var=[10,34,45,56]
conv=tuple(var)
print(conv)

pyth_=[('a',1),('b',0)]
conver=dict(pyth_)
print(conver)


'''
tuple : string;lists
Example
'''
fam=('h','e','l','l','o')
text_2=''.join(fam)
print(text_2)



'''
built-in functions
------------------
str()
float()
int()
list()
dict()
tuple()
'''
