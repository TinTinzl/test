# -*- coding: utf-8 -*-
"""
Created on Fri May 26 10:00:32 2017

@author: lenovo
"""

import pymysql
import string,random

field = string.ascii_letters + string.digits

def getRandom():
    return "".join(random.sample(field,4))

def concatenate(group):
    return "-".join([getRandom() for i in range(group)])

def generate(n):
    codeList = []
    for i in range(n):
        codeList.append(concatenate(4))
    return codeList

def connectmysql(codeList):
    conn = pymysql.connect(
        host='localhost',
        port=3306,
        user='root',
        passwd='123456',
        db='npassword',
        )
    cur = conn.cursor()
    cur.execute("CREATE DATABASE IF NOT EXISTS activation_code")
    cur.execute('USE activation_code')
    cur.execute('''CREATE TABLE IF NOT EXISTS code(
                            id INT NOT NULL AUTO_INCREMENT,
                            code VARCHAR(32) NOT NULL,
                            PRIMARY KEY(id)
                        )''')
    for code in codeList:       
        cur.execute('INSERT INTO code(code) VALUES(%s)',(code))
        cur.connection.commit()
        
    cur.close()
    conn.close()
    
if __name__ == '__main__':
    connectmysql(generate(200))
    print('OK!')


