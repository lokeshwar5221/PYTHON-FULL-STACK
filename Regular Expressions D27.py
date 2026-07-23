'''
Regular Expression(Regex)
---------------------------
--->regex is an sequence of char that can searching patter
--->to use regex we have import re module....
Functions()

1.findall()
-----------
it will find all the char that are in the string...
eg
---
'''
import re
txt = 'python is a language'
print(re.findall('a',txt))

import re
txt = 'python is a Langyuage 1009'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))



'''
2.search()
----------
-->this search will find the char,but it will the first sequence that
found in the string...

eg
---
'''
import re
txt='python is a language and also called dynamically typed'
print(re.search('[a]',txt))



'''
3.split()
---------
eg
---
'''
import re
txt='python is a language and also called dynamically typed'
print(re.split(' ',txt))



'''
4.sub()
--------
eg
---
'''
import re
txt='python is a language and also called dynamically typed'
print(re.sub(' ','&',txt))



'''
5.fullmatch()
-------------
eg
---
'''
import re
txt='i have 100 Rupees'
print(re.findall('[0-9]',txt))
print(re.findall('[a-z]',txt))
print(re.findall('[A-Z]',txt))

print(re.search('[0-9]',txt))
print(re.search('[a-z]',txt))
print(re.search('[A-Z]',txt))

#^
print(re.findall('^i have',txt))
print(re.search('^i have',txt))

#$
import re
some='i am going to school'
print(re.findall('school$',some))
print(re.search('school$',some))

#.
import re
any_='helloo this is loki'
print(re.findall('t..s',any_))
print(re.search('t..s',any_))


#*
import re
how='python module will going complete this week'
print(re.findall('p.*n',how))
print(re.findall('p.*ython',how))
print(re.findall('p.*',how))
print(re.search('p.*n',how))


#+
import re
now='python is a language'
print(re.findall('p.+n',now))
print(re.search('p.+g',now))


#{}
import re
now='python is a language'
print(re.findall('p.{10}',now))
print(re.search('p.{10}',now))
