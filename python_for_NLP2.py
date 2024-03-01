# -*- coding: utf-8 -*-
"""
Created on Thu Aug 17 09:14:41 2023

@author: Dell
"""
#Q identify pattern and extract information?
import re
text='''
Born	Elon Reeve Musk
June 28, 1971 (age 52)
Pretoria, Transvaal, South Africa
Education	University of Pennsylvania (BA, BS)
Title	
Founder, CEO, and chief engineer of SpaceX
CEO and product architect of Tesla, Inc.
Owner and CTO of Twitter
President of the Musk Foundation
Founder of the Boring Company, X Corp., and xAI
Co-founder of Neuralink, OpenAI, Zip2, and X.com (part of PayPal)
Spouses	
Justine Wilson
​
​(m. 2000; div. 2008)​
Talulah Riley
​
​(m. 2010; div. 2012)​
​
​(m. 2013; div. 2016)​
Partner	Grimes (2018–2021)[1]
Children	10[2]
Parents	
Errol Musk
Maye Musk
Family	Musk family
'''
#when we write pattern then we use r before single qute
#we use () when we want specific content like digit
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match(r'age (\d*)',text)
#any single charecter then use dot .
get_pattern_match(r'Born(.*)\n',text).strip()#strip remove white space
get_pattern_match(r'Born.*\n(.*)\(age',text).strip()
get_pattern_match(r'\(age.*\n(.*)',text)

####################################################
def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)\(age',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return {
            'age':int(age),
            'full_name':full_name.strip(),
            'birth_date':birth_date.strip(),
            'birth_place':birth_place.strip()
            }
extract_personal_information(text)
######################################################
text='''
Born:	Dhirajlal Hirachand Ambani
28 December 1932
Chorwad, Junagadh State, British India
(present-day Gujarat, India)
Died	6 July 2002 (age 69)
Mumbai, Maharashtra, India
Citizenship	British India (1932–1947)
Dominion of India (1947–1950)
India(1950–2002)
Occupation	Businessman
Organization(s)	Reliance Industries
Reliance Capital
Reliance Infrastructure
Reliance Power
Spouse	Kokila Dhirubhai Ambani
​
​(m. 1955)​
Children	4, including Mukesh Ambani and Anil Ambani
Awards	Padma Vibhushan (2016) (posthumously)
'''
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match(r'age (\d*)',text)
#any single charecter then use dot .
get_pattern_match(r'Born(.*)\n',text)#strip remove white space
get_pattern_match(r'Born.*\n(.*)\(age',text)
get_pattern_match(r'\(age.*\n(.*)',text)

def extract_personal_information(text):
    age=get_pattern_match('age (\d+)',text)
    full_name=get_pattern_match('Born(.*)\n',text)
    birth_date=get_pattern_match('Born.*\n(.*)',text)
    birth_place=get_pattern_match('\(age.*\n(.*)',text)
    return {
            'age':int(age),
            'full_name':full_name.strip(),
            'birth_date':birth_date.strip(),
            'birth_place':birth_place.strip()
            }
extract_personal_information(text)
##############################################
#Review=it is unstructure data
#set of sentences is called as document
#tokanization = 1) words token 2) sentence tokenization
##################################################
#Tokanization
#split( ) function convert string in to list
txt="welcome to the new year 2023"
x=txt.split()
print(x)
##########################################################
#Removing special charecter
#sub=subtitude with nothings
import re
def remove_special_charecters(text):
    #define the pattern to keep
    pat =r'[^a-zA-z0-9.,!?/"\'\s]'
    return re.sub(pat,'',text)
#function call

remove_special_charecters("007 Not sure@ if this  % was # fun !558923 what do # you think** of it ")
   
###################################################
#removing numbers
import re
def remove_special_charecters(text):
     #define the pattern to keep
     pat =r'[^a-zA-z.,!?/"\'\s]'
     return re.sub(pat,'',text)
 #function call
remove_special_charecters("007 Not sure@ if this  % was # fun !558923 what do # you think** of it ")
  
 ######### ##################################
txt ="welcome:to the,new year;2023"
import re
x=re.split(r'(?:,/;/\s)\s*',txt)
print(x)   
####################################################33
#removing punctuation
#import
import string #function  to remove punctuation
def remove_punctuation(text):
     text=''.join([c for c in text if c not in string.punctuation])
     return text#call function
remove_punctuation('Article:@First sentence of some,{important}article having lot of ~ punctuations And another one;!') 
####################################################
#stemming
#steming is the process of reducing base or root
 
import nltk#function for stemming
def get_stem(text):
    stemmer = nltk.porter.porterStemmer()
    text = ''.join([stemmer.stem(word)for word in text.split()])
    return text #call function
get_stem("we are eating and swimming we havebeen eating and swimming;he eats and swims;he ate and swam ")