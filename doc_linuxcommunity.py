# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 16:35:12 2019

@author: YJIANG14
"""

import requests
import re
#from lxml import etree


def savedata(text):
    with open('cotent.txt', 'a', encoding='utf-8') as f:
        f.write(text)
        
url_org = "https://linux.linuxidc.com/"
data_years = requests.get(url_org)

url_years_list = re.findall(r'<img src="linuxconf/icons/folder.png"> <a href="(.*?)">', data_years.text)
years_list = re.findall(r'<img src="linuxconf/icons/folder.png"> <a href=".*?">(.*?)</a>', data_years.text)
#print(years_list) 
#print(url_years_list[1:-1])
for url_years_one, years in zip(url_years_list[1:-1], years_list[1:-1]):
#    print(url_years_one)
#    print(years)
#    savedata(years+'\n')
    
    url_years = "https://linux.linuxidc.com/" + url_years_one
#    print(url_years)
    
    data_months = requests.get(url_years)

    url_months_list = re.findall(r'<img src="linuxconf/icons/folder.png"> <a href="(.*?)">', data_months.text)
    months_list = re.findall('<img src="linuxconf/icons/folder.png"> <a href=".*?">(.*?)</a>', data_months.text)
    
    for url_months_one, months in zip(url_months_list, months_list):
#        print(months)
#        savedata(months+'\n')
        
        url_months = "https://linux.linuxidc.com/" + url_months_one
        data_days = requests.get(url_months)
        url_days_list = re.findall(r'<img src="linuxconf/icons/folder.png"> <a href="(.*?)">', data_days.text)
        days_list = re.findall(r'<img src="linuxconf/icons/folder.png"> <a href=".*?">(.*?)</a>', data_days.text)
        
        for url_days_one, days in zip(url_days_list, days_list):
#            print(days)
#            savedata(days+'\n')
            url_days = "https://linux.linuxidc.com/" + url_days_one
            data_docs = requests.get(url_days)
            docs = re.findall(r'<img src="linuxconf/icons/folder.png"> <a href=".*?">(.*?)</a>', data_docs.text)
            for doc in docs:
                print(years)
                print(months)
                print(days)
                print(doc)
                savedata(years + ' ')
                savedata(months + ' ')
                savedata(days + '\n')
                savedata(doc+'\n')
            

            
        
  
        
       

        


    
       
    

