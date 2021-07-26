# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 11:34:09 2021

@author: dkjua
"""
mylist=[]
u=0
i=0
y=int(input('人數?'))
while i<int(y):
    x=int(input('成績?'))
    mylist.append(x)
    i=i+1
    u=u+x
print(mylist)
print(float(u//y))
