# -*- coding: utf-8 -*-
"""
Created on Fri Jun 16 20:25:33 2017

@author: ZhuLiang
"""

from urllib.request import urlopen  
from bs4 import BeautifulSoup  
import sys

html = urlopen("https://www.nowcoder.com/ta/review-java")  
bsObj=BeautifulSoup(html,"lxml")    #将html对象转化为BeautifulSoup对象  
liList=bsObj.findAll("td",{"class":"txt-left"})
for ul in liList:
    ul2 = ul.findAll("a",{"target":"_blank"})
    for ul3 in ul2:
        print('https://www.nowcoder.com/ta'+ul3.get('href'))
    