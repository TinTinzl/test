# -*- coding: utf-8 -*-
"""
Created on Wed Jun 14 21:21:53 2017

@author: ZhuLiang
"""

import time,sys,queue
from multiprocessing.managers import BaseManager

class QueueManager(BaseManager):
    pass
def calcu():
    #register queue to network
    QueueManager.register('get_task_queue')
    QueueManager.register('get_result_queue')

    #connect to server machine...
    server_addr='127.0.0.1'
    print('Connect to server %s...'%server_addr)
    #set port and address
    m=QueueManager(address=(server_addr,5000),authkey=b'abc')
    #connectint...
    m.connect()
    #get queue info
    task=m.get_task_queue()
    result=m.get_result_queue()
    #get content from task queue and return new result to result queue
    for i in range(10):
        try:
            n=task.get(timeout=1)
            print('run task %d*%d...'%(n,n))
            r='%d*%d=%d'%(n,n,n*n)
            time.sleep(1)
            result.put(r)
        except queue.Empty:
            print('task queue is empty...')
    print('worker exit...')