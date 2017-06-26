# -*- coding: utf-8 -*-
"""
Created on Wed May 31 11:07:18 2017

@author: ZhuLiang
"""

from PIL import Image
import os
import tkinter as tk 
import tkinter.filedialog

path = ''
resultPath = ''
def openflie():
    default_dir = r"C:\Users\lenovo\Desktop\python\WorkBook"
    fname = tkinter.filedialog.askopenfilename(title=u"选择读入图片路径",
                                     initialdir=(os.path.expanduser(default_dir)))
    return fname

def saveflie():
    default_dir = r"C:\Users\lenovo\Desktop\python\WorkBook"
    fname = tkinter.filedialog.askopenfilename(title=u"选择保存图片路径",
                                     initialdir=(os.path.expanduser(default_dir)))
    return fname

def exchangeimage():
    path = openflie()
    resultPath = saveflie()
    if not os.path.isdir(resultPath):
        os.mkdir(resultPath)
    for picName in os.listdir(path):
        picPath = os.path.join(path, picName)
        print(picPath)
        with Image.open(picPath) as im:
            w, h = im.size
            n = w / 1366 if (w / 1366) >= (h / 640) else h / 640
            im.thumbnail((w / n, h / n))
            im.save(resultPath+'/finish_' + picName.split('.')[0] + '.jpg', 'jpeg')
            
if __name__ == '__main__':
    root = tk.Tk() 
    tk.Button(root,text='open',command=exchangeimage).pack() 
    root.mainloop()