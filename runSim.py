#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  4 10:42:42 2019

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
ab = h.EdgeServer(5,[a,b])
cd = h.EdgeServer(6,[c,d])
abcd = h.CentralHeatingSys(7,[ab,cd])

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
listofnodes = [a,b,c,d]
i= 1
for node in listofnodes:
    print("starting thread " + str(i))
    threading.Thread(target = node.run).start()
    i = i+1
