#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 15:52:51 2019

@author: mihirwagle
"""

import HVAC as h
import threading
import time

start = time.time()
threshold = 100
a = h.HVAC(1,threshold,start)
b = h.HVAC(2,threshold,start)
c = h.HVAC(3,threshold,start)
d = h.HVAC(4,threshold,start)
e = h.HVAC(5,threshold,start)
f = h.HVAC(6,threshold,start)
g = h.HVAC(7,threshold,start)
h0 = h.HVAC(8,threshold,start)
i = h.HVAC(9,threshold,start)
j = h.HVAC(10,threshold,start)
k = h.HVAC(11,threshold,start)
l = h.HVAC(12,threshold,start)
m = h.HVAC(13,threshold,start)
n = h.HVAC(14,threshold,start)
o = h.HVAC(15,threshold,start)
p = h.HVAC(16,threshold,start)
q = h.HVAC(17,threshold,start)
r = h.HVAC(18,threshold,start)
s = h.HVAC(19,threshold,start)
t = h.HVAC(20,threshold,start)
u = h.HVAC(21,threshold,start)
v = h.HVAC(22,threshold,start)
w = h.HVAC(23,threshold,start)
x = h.HVAC(24,threshold,start)
abcd = h.EdgeServer(25,[a,b,c,d,e])
efgh = h.EdgeServer(26,[e,f,g,h0,i])
ijkl = h.EdgeServer(27,[i,j,k,l,m])
mnop = h.EdgeServer(28,[m,n,o,p,q])
qrst = h.EdgeServer(29,[q,r,s,t,u])
uvwx = h.EdgeServer(30,[u,v,w,x,a,ijkl])
CHS = h.CentralHeatingSys(31,[abcd,efgh,ijkl,mnop,qrst,uvwx,a])

# Check for proper connections.
#x = abcd.children
#for element in x:
#    print(element.getID())
#x = ab.children
#for element in x:
#    print(element.getID())
#x = cd.children
#for element in x:
#    print(element.getID())
listofnodes = [a,b,c,d,e,f,g,h0,i,j,k,l,m,n,o,p,q,r,s,t,u,v,w,x]
i= 1
for node in listofnodes:
    print("starting thread " + str(i))
    threading.Thread(target = node.run).start()
    i = i+1
