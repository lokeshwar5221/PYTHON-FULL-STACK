'''
#Every Python file -->Module -->import keyword-->__name__-->
import Day4 
print(dir(Day4))#dir-->directory will return all available method,zttributes
print(type(Day4.details))
print(type(Day4.employee))
Day4.employee('loki',department='csd',location='vizag')
print(Day4.details.keys())
print(Day4.details['branches'])
Day4.details.update({'batches':['pfs','da','jfs','aiml'],'employees':250})
print(Day4.details)

#from Keyword
import Day4
from Day4 import employee,details
details.update({'batches':['pfs','da','jfs','aiml'],'employees':250})
print(details)
print(Day4.__doc__)#return doc string from the given module
'''
#Built-in modules-->math,random,os,time,datatime

#we can download module-->pypi(python package index)

#Build a QRcode Scanner for your linkedin and github profile
import pyqrcode
import png
link='https://www.linkedin.com/in/kakumanu-lokeshwar-32a55a417'
qr=pyqrcode.create(link)
#print(qr)
qr.png("loki_linkedin.png",scale=10)
