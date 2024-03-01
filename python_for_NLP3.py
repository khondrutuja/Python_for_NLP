# -*- coding: utf-8 -*-
"""
Created on Mon Aug 21 08:50:54 2023

@author: Dell
"""
#now we have multiple file and we have to find perticular file
import re
line = 'asdf fidk; afed,fjek,asdf,foo'
re.split(r'(?:,|;/\s)\s*',line)
###########################################
#maching text at the start or end of string
filename='spam.txt'
filename.endswith('.txt')
###############################
area_name='6th lane west Andheri'
area_name.endswith('west Andheri')
###############################
choices=('http:','ftp:')
url='http://www.python.org'
url.startswith(choices)
###################################
#Slicing a string
#if S is a string the expression s[start:stop:steps]
#return the portion of the string from index start to
#at s step size step.
S = 'ABCDEFGHI'
print(S[2:7])   #CODGF
#note that item at index 7 'H' is not included.
#Slice with NEgative Indices
S='ABCDEFGHI'
print(S[-7:-2])
#CDEFG
#slicing with positive negative index
#IMP
S='ABCDEFGHI'
print(S[2:-5]) #CD


S='ABCDEFGHI'
print(S[2:7:2]) #CD
#return every second item

S='ABCDEFGHI'
print(S[6:1:-2])
##########################
#slice first therr charecter from the string
S='ABCDEFGHI'
print(S[:3])
####################################
#slice last three charecter
S='ABCDEFGHI'
print(S[6:])
#################################
#reversing the string
#you can revers the string by ommiting both start and stop indices
S='ABCDEFGHI'
print(S[::-1])
################################
#similar opration can be done with slices
filename='spam.txt'
filename[-4]=='.txt'
#################################
url = 'https://www.python.org'
url[:5]=='http:' or url[:6]=='https:' or url[:4]=='ftp:'
##############################################
#IMP
from fnmatch import fnmatch,fnmatchcase
names = ['Andheri East','Parle East','Doadar West']
[name for name in names if fnmatch(name,'* East')]
#['Andheri East', 'Parle East']
##############################################
#pip install fnmatch2
addressess =[
    '5412N CLARK SK',
    '4452 ADDSION ST'
    '3443 JDOSS GH',
    '4858 RGIVV NV']
from fnmatch import fnmatch,fnmatchcase
[add for add in addressess if fnmatchcase(add,'*ST')]
#########################################################
#when we want to extract perticular text  in feature ingineering
text = 'yeah,but no,but yeah,but no,but yeah'
#Exact match
text=='yeah'
text.startswith('yeah')
text.endswith('no')
text.find('no')
##################################################
#/maching pattern
text1='11/27/2021'
text2='Nov 27,2012'
import re
#simple macing:-\d+ means match one or more digits
if re.match(r'\d+/|d+/\d+',text1):
    print('yes')
else:
    print('no')
if re.match(r'\d+/\d+/\d+',text2):
    print("yes")
else:
    print("no")    
#######################################################
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
if re.match(datepat,text1):
    print("yes")
else:
    print("no")
if re.match(datepat,text2):
    print("yes")
else:
    print("no")
#####################################################
#searching and replacing the text
text = 'yeah,but no,but yeah,but no,but yeah' 
text.replace('yeah','yep')    
################################################
#if you have dates in formate 11/27/2012 want to convert 2012-1
text='Today is 11/27/2012.pyCon start 3/13/2013.'
import re
re.sub(r'(\d+)/(\d+)/(\d+)',r'\3-\1-\-2',text)
#\3 3rd group,\1 st group
#############################################
#if you want to know how many subtitution are
#made in text then
#you can use subn() method
newtext,n=datepat.subn(r'\3-\1-\-2',text)
newtext
###############################################
text='UPPER PYTHON,Lower python,Mixed python'
re.findall('python',text,flags=re.IGNORECASE)
#TO SUBTITUDE
re.sub('python','snake',text,flags=re.IGNORECASE)
#'UPPER snake,Lower snake,Mixed snake'
##################################################
#the last reveals 
import re
def matchcase(word):
    def replace(m):
        text = m.group()
        if text.isupper():
            return word.upper()
        else: text.word.upper()
            return word.lower()
        elif text[0].isupper():
              return word.capitalize()
        else:
            return word
        return replace 
text3=re.sub('python',matchcase('snake'),text,flags=re.IGNORECASE) 
text3   
###############################################33
str_pat =re.compile(r'\"(.*)\"')
text1='computer says "no"'
str_pat.findall(text1)
###############################################
text2='computer says "no." phone says "yes."'
str_pat.findall(text2)
#############################################
str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2)
####################################
comment = re.compile(r'/\*(*?)\*')
text1 = '/*this is a comment */'
comment.findall(text1)
######################################
text2 = '''/* this is a multiline comment */
'''
comment.findall(text2)
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2)
 
comment = re.compile(r'/\*(.*?)\*/',re.DOTALL)
comment.findall(text2)
#####################################
#what is encoding and  ##IMP
#encoding=   transformation of human language in to binary formate
#Normalization:- unicode text to stander
#UTF=8,16,32
s1='spicy jalape\u00f10'
s2='spicy Jalapen\u03030'
print(s1)
print(s2)
s1==s2

import unicodedata
t1 = unicodedata.normalize('NFC',s1)
t2=  unicodedata.normalize('NFC',s2)
t1==t2
print(ascii(t1))