# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 15:43:11 2021

@author: dkjua
"""
mylist=[]
i=0
u=0
y=int(input('人數?'))
while i<int(y):
    x=int(input('成績?'))
    mylist.append(x)
    i=i+1
    if u<x:
        u=x
print('最高成績:'+str(u))
