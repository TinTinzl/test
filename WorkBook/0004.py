# -*- coding: utf-8 -*-
"""
Created on Wed May 31 09:56:03 2017

@author: lenovo
"""

import re

fin = open('1.txt', 'r')
str = fin.read()

reObj = re.compile('\b?(\w+)\b?')
words = reObj.findall(str)

wordDict = dict()

for word in words:
    if word.lower() in wordDict:
        wordDict[word.lower()] += 1
    else:
        wordDict[word] = 1
                
for key, value in wordDict.items():
    print('%s: %s'% (key, value))