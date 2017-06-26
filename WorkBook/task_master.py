# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:21:24 2017

@author: ZhuLiang
"""

import random,time,queue,threading
from multiprocessing.managers import BaseManager
from multiprocessing import freeze_support#>>>>2.modify:add this if your system is windows
from task_worker import calcu#task_worker.py
#send mession queue
task_queue=queue.Queue()
#receive mession queue 
result_queue=queue.Queue()

#heir form Base...
class QueueManager(BaseManager):
    pass
#>>>>1.modify:replace lamda expression with function def task...
def task_q():
    return task_queue
def result_q():
    return result_queue

def test():
    #register two queue to network and connect  para callable to object Queue
    QueueManager.register('get_task_queue',callable=task_q)
    QueueManager.register('get_result_queue',callable=result_q)
    #binding port:5000 and set password 'abc'
    manager=QueueManager(address=('127.0.0.1',5000),authkey=b'abc')
    #launch queue
    manager.start()
    #get object queue from network
    task=manager.get_task_queue()
    result=manager.get_result_queue()
    #set mession
    for i in range(10):
        n=random.randint(0,10000)
        print('Put task %d...'%n)
        task.put(n)
    #get result from queue
    print('Try to get results...')
    for i in range(10):
        r=result.get(timeout=10)
        print('Result:%s'%r)
    #close
    manager.shutdown()
    print('master exit.')

if __name__=='__main__':
    freeze_support()#>>>>2.modify:add this if your system is windows
    t1=threading.Thread(target=test,name='master')
    t2=threading.Thread(target=calcu,name='worker')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('Done...')