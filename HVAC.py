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
    def __init__(self, idd, threshold,start):
        self.start = start
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
        while True and time.time()< start + 100:
            time.sleep(0.1)
            self.temp += random.randrange(-1.0,1.0)
            if self.temp < 80 or self.temp > 120:
                self.temp = random.randrange(90.0,110.0)
            #print(str(self.getID()) + " : " + str(self.temp))
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
        else:
            lister = list()
            for child in self.listErrantNodes:
                lister.append(child.getID())
            print(lister)
    
    def removeErrant(self, node):
        self.listErrantNodes.discard(node)
        if len(self.listErrantNodes) == 0:
            print("")
        else:
            lister = list()
            for child in self.listErrantNodes:
                lister.append(child.getID())
            print(lister)

start = time.time()
threshold = 100
a = HVAC(1,threshold,start)
b = HVAC(2,threshold,start)
c = HVAC(3,threshold,start)
d = HVAC(4,threshold,start)
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
listofnodes = [a,b,c,d]
i= 1
for node in listofnodes:
    print("starting thread " + str(i))
    threading.Thread(target = node.run).start()
    i = i+1