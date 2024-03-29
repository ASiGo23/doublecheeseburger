#!/usr/bin/python

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
        elif (self.base == self.top):
            self.base.next = node
            node.previous = self.base
        else: 
            self.top.next = node
            node.previous = self.top

        self.top = node

    def forward(self, 
                func, 
                parameter,
                restrict:type = None, 
                threads:int = 1, 
                processes:int = 1):
        self.base.forward(func, parameter, restrict, threads, processes)
