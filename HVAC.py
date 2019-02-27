#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 27 08:52:01 2019

@author: mihirwagle
"""

import random


class HVAC:
    def __init__(self, idd, threshold):
        self.idd = idd
        self.temp = random.randrange(-20,35)
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
            self.temp += random.randrange(-1,1)
            if self.flag == 0:
                if self.temp >= self.threshold:
                    # logic for update with locking
                    self.flag = 1
            else:
                if self.temp < self.threshold:
                    # logic for update with locking
                    self.flag = 0
        # this runs forever
        
    def addParent(self, parent):
        self.parents.add(parent)
    
    def getID(self):
        return self.idd


class EdgeServer:
    def __init__(self, idd, childrenlist):
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
            # lock
            parent.addErrant(node)

    def removeErrant(self, node):
        self.listErrantNodes.discard(node)
        for parent in self.parents:
            # lock
            parent.removeErrant(node)


class CentralHeatingSys:
    def __init__(self, idd, childrenlist):
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
    
    def removeErrant(self, node):
        self.listErrantNodes.discard(node)

threshold = 100
a = HVAC(1,100)
b = HVAC(2,100)
c = HVAC(3,100)
d = HVAC(4,100)
ab = EdgeServer(5,[a,b])
cd = EdgeServer(6,[c,d])
abcd = CentralHeatingSys(7,[ab,cd])

# Check for proper connections.
x = abcd.children
for element in x:
    print(element.getID())
x = ab.children
for element in x:
    print(element.getID())
x = cd.children
for element in x:
    print(element.getID())