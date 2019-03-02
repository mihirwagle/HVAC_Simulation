#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:52:01 2019

@author: mihirwagle
"""

import random
import time
import threading

class HVAC:
    def __init__(self, idd, threshold):
        self.idd = idd
        self.temp = random.randrange(90.0,110.0)
        self.threshold = threshold
        self.parents = set()
        self.flag = 0
        #self.run()
    
    def run(self):
        if self.temp >= self.threshold:
            self.flag = 1
        else:
            self.flag = 0
        while True:
            time.sleep(0.1)
            self.temp += random.randrange(-1.0,1.0)
            if self.temp < 80 or self.temp > 120:
                self.temp = random.randrange(90.0,110.0)
            print(str(self.getID()) + " : " + str(self.temp))
            if self.flag == 0:
                if self.temp >= self.threshold:
                    # logic for update with locking
                    for parent in self.parents:
                        with parent.lock:
                            parent.addErrant(self)
                    self.flag = 1
            else:
                if self.temp < self.threshold:
                    # logic for update with locking
                    for parent in self.parents:
                        with parent.lock:
                            parent.removeErrant(self)
                    self.flag = 0
        # this runs forever
        
    def addParent(self, parent):
        self.parents.add(parent)
    
    def getID(self):
        return self.idd


class EdgeServer:
    def __init__(self, idd, childrenlist):
        self.lock = threading.Lock()
        self.idd = idd
        self.parents = set()
        self.children = set()
        self.listErrantNodes = set()
        for child in childrenlist:
            child.getID()
            self.addChild(child)
    
    def addParent(self, parent):
        self.parents.add(parent)
    
    def addChild(self, child):
        self.children.add(child)
        child.addParent(self)
    
    def getID(self):
        return self.idd
    
    def addErrant(self, node):
        self.listErrantNodes.add(node)
        for parent in self.parents:
            with parent.lock:
                parent.addErrant(node)

    def removeErrant(self, node):
        self.listErrantNodes.discard(node)
        for parent in self.parents:
            with parent.lock:
                parent.removeErrant(node)


class CentralHeatingSys:
    def __init__(self, idd, childrenlist):
        self.lock = threading.Lock()
        self.idd = idd
        self.children = set()
        self.listErrantNodes = set()
        for child in childrenlist:
            self.addChild(child)
    
    def addChild(self, child):
        self.children.add(child)
        child.addParent(self)
        
    def getID(self):
        return self.idd
    
    def addErrant(self, node):
        self.listErrantNodes.add(node)
        if len(self.listErrantNodes) == 0:
            print("")
        for node in self.listErrantNodes:
            print(node.getID())
    
    def removeErrant(self, node):
        self.listErrantNodes.discard(node)
        if len(self.listErrantNodes) == 0:
            print("")
        for node in self.listErrantNodes:
            print(node.getID())

threshold = 100
a = HVAC(1,100)
b = HVAC(2,100)
c = HVAC(3,100)
d = HVAC(4,100)
ab = EdgeServer(5,[a,b])
cd = EdgeServer(6,[c,d])
abcd = CentralHeatingSys(7,[ab,cd])

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

t1 = threading.Thread(target = a.run()).start()
t1.daemon = True
t2 = threading.Thread(target = b.run()).start()
t2.daemon = True
t3 = threading.Thread(target = c.run()).start()
t3.daemon = True
t4 = threading.Thread(target = d.run()).start()
t4.daemon = True

#t1.start()
#t2.start()
#t3.start()
#t4.start()