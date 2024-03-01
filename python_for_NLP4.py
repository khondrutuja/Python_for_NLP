# -*- coding: utf-8 -*-
"""
Created on Tue Aug 22 08:17:40 2023

@author: Dell
"""

#IMP = what is UTF (unocode transfornation formate)
#unicode only define code points,that is a number which represents 
# a charexter
string1='apple'
string2="jeeil25"
string3="pre@12"
string4='pre@12'
string1.encode(encoding='UTF-8',errors='strict')
string2.encode(encoding='UTF-8',errors='strict')
string3.encode(encoding='UTF-8',errors='strict')
string4.encode(encoding='UTF-8',errors='strict')
#############################################
text='one 🐘 and three 🐋'
print(text)
print(len(text))
'''
we encode the string in to bytes type using the utf8 encoding and
and print the bytes.
we count the number of bytes in this

'''
e= text.encode('utf8')
print(e)
print(len(e))

e=text.encode('utf16')
print(e)
print(len(e))

with open(fname,mode='rb')as f:
    #by default it encide in utf8
    contents = f.read()
    print(type(contents))
    print(contents)
    print(contents.decode('utf-8')) #not 
###################################
#Striping unwanted charecter from string
#you want to remove unwanted charecter like white space
#string.lstrip() and rstrip() perform stripping
#Whitespace stripping
s = 'hello world \n'
s.strip()
#'hello world'
######################################
s = 'hello world \n'
s.lstrip()
######################################
s = 'hello world \n'
s.rstrip()
#################################
#charecter stripping
t = '----hello======'
t.lstrip('-')
#'hello======'
t.strip('-=')
#'hello'
#######################################
s = 'hello world \n'
s.strip()
s
s.replace('','')
####################################
#we also use re/regex library
import re
re.sub('\s+','',s)
########################################
#Alignment the text string
text="Hello World"
text.ljust(20)#add space of 20 charecter to right side
#'Hello World         '
text.rjust(20)
#
text.center(20)
#############################################
#All of these methods accepts an optional
text.rjust(20,'=')
text.center(20,'*')
############################################
format(text,'>20')
format(text,'<20')
format(text,'^20')
#^ cap is for center
####################################################33333
#Here you can charecter to fill the space at left,right
#charecter:
format(text,'=>20')
format(text,'*^20s')    
######################################################
#These format codes can also be use in the formate() method
'{:>10s}{:>10s}'.format('hello','world')
#one benifet of format() is what it is not specific to string
#making it more general purpose.For instance,you can use it
x=1.2345
format(x,'>10')
x

format(x,'^10.2f')
############################################################
#IMP
parts = ['IS','chicago','Not','chicago']
''.join(parts)
','.join(parts)
''.join(parts)
#############################################################
