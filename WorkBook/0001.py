# -*- coding: utf-8 -*-
"""
Created on Fri May 26 09:35:11 2017

@author: lenovo
"""

import string,random

field = string.ascii_letters + string.digits

def getRandom():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

def generate(n):
    return [concatenate(4) for i in range(n)]

if __name__ == '__main__':
    print (generate(200))