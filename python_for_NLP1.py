# -*- coding: utf-8 -*-
"""
Created on Wed Aug 16 09:17:55 2023

@author: Dell
"""
#go to google tesla company filling
#tsla-20230630-gen.pdf 
#after that regex101.com
#regex101.com then click below link
#regex101: build, test, and debug regex
#go to anaconda navigator and go to enverment and  go 
#to base terminal-> open terminal
#and type pip install regex
import re  #re=regular expression
text='''
      Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern = '\d\d\d\d\d\d\d\d\d\d' #\d = back slash d represent didit.
matches=re.findall(pattern,text)
matches

#we want exactly 3 time  each number
text='''
      Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern=r'\d{3}'
matches=re.findall(pattern,text)
matches
#######################
#IMP=NLP pattern =feature engineering
#we want=[(999)-333-7777]
#\(\d{3}\)-\d{3}=breakets , we want breaket (999)
pattern='\(\d{3}\)-\d{3}-\d{4}'
matches=re.findall(pattern,text)
matches 
##########################
#now we want alternater match either a or b
#in this case use | (paip) and write two expression in only one singel quat
text='''
      Elon musk's phone number is 9991116666, call him if you have any questions on dodgecoin. Tesla's revenue is 40 billion
Tesla's CFO number (999)-333-7777 and tesla's revenue is 20 billion
'''
pattern='\(\d{3}\)-\d{3}-\d{4}|\d{10}'
matches=re.findall(pattern,text)
matches
############################################3
#we want to remove a specific character means semicolan and -(hypan)
'''
let us try
following pattern
A protracted; legal battle; over a 32-carat;
 Golconda diamond-
 we want charecter ecept ; and -
 pattern will be [^;-]=except
 go to regular expression window and type thise pattern
 '''
#if we dont want any symboll then write that symboll in squre breaket. 
text2='A protracted; legal battle; over a 32-carat;Golconda diamond-'
pattern='[^;-]'
matches=re.findall(pattern,text)
matches 
#################################
#report
#want summary on  report we want to extract patte 
#when you want only one line not next line[^\n]
#pattern='Note \d - [^\n]+'
#
import re
text3='''
Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of
June 30, 2023, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of
redeemable noncontrolling interests and equity for the three and six months ended June 30, 2023 and 2022, and the consolidated statements of cash
flows for the six months ended June 30, 2023 and 2022, as well as other information disclosed in the accompanying notes, are unaudited. The
consolidated balance sheet as of December 31, 2022 was derived from the audited consolidated financial statements as of that date. The interim
consolidated financial statements and the accompanying notes should be read in conjunction with the annual consolidated financial statements and the
accompanying notes contained in our Annual Report on Form 10-K for the year ended December 31, 2022.
The interim consolidated financial statements and the accompanying notes have been prepared on the same basis as the annual consolidated
financial statements and, in the opinion of management, reflect all adjustments, which include only normal recurring adjustments, necessary for a fair
statement of the results of operations for the periods presented. The consolidated results of operations for any interim period are not necessarily
indicative of the results to be expected for the full year or for any other future years or interim periods.
'''
pattern='Note \d - [^\n]'
matches=re.findall(pattern,text3)
matches 

pattern='Note \d - [^\n]+' #+ means all string 'Note \d - [^\n]*'
matches=re.findall(pattern,text3)
matches 
##########################################
#we want  only summary of account policy
#we want content after -(hypen)
#capture everything enclosed(-----) # * and + are same
pattern='Note \d - ([^\n]*)'
matches=re.findall(pattern,text3)
matches 
##############################################
#1 qurter=3 months
#we want to extract financial  reporting
text4='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r"FY\d{4} Q\d"
matches=re.findall(pattern,text4)
matches 
################################################
text4='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r"FY\d{4} Q[1234]"
matches=re.findall(pattern,text4)
matches 
#########################################################
text4='''
The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion. The gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. FY2020 Q4 it was $3 billion.
'''
pattern=r"FY\d{4} Q[1-4]"
matches=re.findall(pattern,text4)
matches 
################################################
#what your text compreses of


text5='''
he gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern1=r"FY\d{4} Q[1-4] |fy\d{4} Q[1-4]"

matched=re.findall(pattern1.text5)
matched

text5= '''  
he gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
'''
pattern1=r"FY\d{4} Q[1-4] |fy\d{4} Q[1-4]"

matched=re.findall(pattern1.text5)
matched
#another way
matched=re.findall(pattern,text5,re.IGNORECASE)
matched # not exicute
###################################'''
pattern='FY(\d{4} Q[1-4])'
matched=re.findall(pattern,text5,re.IGNORECASE)
matched
##################################'''
#we want $4.85 and $3
#simply $ can not be use as it is special symbol
#pl refer right bottom window
#Even . charecter can not be used it is also a special symboll
text6= '''
he gross cost of operating lease vehicles in FY2021 Q1 was $4.85 billion.
In previous quarter i.e. fy2020 Q4 it was $3 billion.
 '''' '''
pattern='\$[0-9\.]+'
matched=re.findall(pattern,text6)
matched
#######################################
#if we do not want $
pattern='\$([0-9\.]+)'
matched=re.findall(pattern,text6)
matched

###########################################
#pip install PyPDF2
#whenever install pakege the always restart the kernal
from PyPDF2 import PdfFileReader
#importing required module
from PyPDF2 import PdfReader
#creating pdf reader object
reader=PdfReader('c:/1-python/python_tutorial.pdf')
#printing the number of specific page
print(len(reader.pages))
#getting specific page from pdf
page=reader.pages[10]
#extracting text from page
text=page.extract_text()
print(text)
#################################
import re
text7='Hi:-I have a problem with my order number 412889912'
pattern='order[^\d]*(\d*)'
matched=re.findall(pattern,text7)
matched
###################################################
import re
chat2='Hi:-I have a problem with my order number 412889912'
pattern='order[^\d]*(\d*)'
matched=re.findall(pattern,chat2)
matched

import re
chat1='Hi:-I have a problem with my order number #412889912'
pattern='order[^\d]*(\d*)'
matched=re.findall(pattern,chat1)
matched
#########################################
chat3='Hi: My order 412889912 is having an issue,I was charged 300$ when'
pattern='order[^\d]*(\d*)'
matched=re.findall(pattern,chat3)
matched
##################################
def get_pattern_match(pattern,text):
    matches=re.findall(pattern,text)
    if matches:
        return matches[0]
get_pattern_match('order[^\d]*(\d*)',chat1)    
#######################################
chat1='Hi: you ask lot of question 1235678912,abc@xyz.com'
chat2='Hi:here  it is:(123)-567-8912,abc@xyz.com'
chat3='Hi:yes,phone:1235678912 email:abc#xyz.com'
get_pattern_match('[a-zA-Z0-9_]*@[a-z]*\.[a-zA-Z0-9)]*',chat2)
    


