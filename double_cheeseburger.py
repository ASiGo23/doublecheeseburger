#!/usr/bin/python

from functools import partialmethod


class node():
    def __init__(self):
        self.next       = None
        self.previous   = None
        self.type_next      = None
        self.type_previous  = None
        return self
    
    def forward(self, 
                func, 
                parameter,
                restrict:type = None, 
                threads:int = 1, 
                processes:int = 1):
        if (restrict == None or isinstance(self, restrict)) and self.type_next != None:
            func(self,parameter)
            self.type_next.forward(func, parameter, restrict, threads, processes)
        elif self.next != None:
            self.next.forward(func, parameter, restrict, threads, processes)
class double_linked_list():
    def __init__(self, list:list = []):
        self.length = 0
        self.base = None
        self.top = None
        for node in list:
            self.append(node)
    
    def append(self, node:node):
        self.length += 1
        if (self.base) == None:
            self.base = node
            self.top = node
        self.top.next = node
        self.top = node

    def forward(self, 
                func, 
                parameter,
                restrict:type = None, 
                threads:int = 1, 
                processes:int = 1):
        self.base.forward(func, parameter, restrict, threads, processes)

class burger(node):
    def __init__(self):
        super().__init__()
    def func(self,param):
        print(param)

joe = double_linked_list([burger(),burger()])
joe.forward(burger.func, "cheese")