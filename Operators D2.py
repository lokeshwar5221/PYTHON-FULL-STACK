'''OPERATORS
---------
1.Arithmetic operator
---------------------
-->+,-,*,/,%,**  
eg->'''
a=10
b=20
print(a+b,a-b,a*b,a/b,a%b)
'''
2.Assignment operator
---------------------
-->+=(increment),-=(decrement),*=,/=
eg-->
'''
a=10
b=10
c=10
d=10
a+=5
b-+5
c*=5
d/=5
print(a,b,c,d)
'''
3.Comparision operator
----------------------
-->==,!=,>=,<=
eg-->'''
a=10
b=20
print(a==b,a>=b,a<=b,a!=b,a>b,a<b)
'''
4.Logical operator
------------------
  1.And->Returns true if both are true
  2.OR->Return true if any one is correct
  3.NOT->Reverse the output
eg-->
'''
a=10
b=20
c=30
print(a>=b and b>=c)
print(a>=b or b>=c)
print(not(a>=b or b>=c))
'''
5.Identity operator
-------------------
is->same object or not
is not->not the same object
eg-->
'''
a=20
b=2
print(a is b)
print(a is not b)

'''
6.Membership operator
---------------------
in->checks whether the given number is there or not
not in->checks whether the given number is there or not
eg->
'''
c=[1,2,4,67,8]
print(2 in c)
print(2 not in c)
'''
7.Bitwise operator
------------------
&,<<,>>,|,^
eg->
'''
print(5&3)
print(5|4)
