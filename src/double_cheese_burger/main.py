#!/usr/bin/python

from functools import singledispatchmethod

class node():
    def __init__(self, info):
        self.info = info
        self.next       = None
        self.previous   = None
        self.type_next      = None
        self.type_previous  = None
    
    def forward(self, 
                func, 
                parameter,
                restrict = None):
        value = func(self, parameter)
        if restrict == None:
            return(self.next, value)
        else:
            return(self.type_next, value)
class double_linked_list():
    def __init__(self, iterable = None):
        self.length = 0
        self.base = None
        self.top = None

        self.type_base = {}
        self.type_top = {}

        if iterable == None:
            return
        for layer in iterable:
            self.append(node(layer))
    
    @singledispatchmethod
    def append(self, info):
        self.node_append(node(info))

    @append.register 
    def node_append(self, node:node):
        self.length += 1
        if (self.base) == None:
            self.base = node
        elif (self.top == None):
            self.base.next = node
            node.previous = self.base
            self.top = node
        else: 
            self.top.next = node
            node.previous = self.top
            self.top = node

        if type(node.info).__name__ not in self.type_base:
            self.type_base[type(node.info).__name__] = node
            return
        elif type(node.info).__name__ not in self.type_top:
            self.type_base[type(node.info).__name__].type_next = node
            node.type_previous = self.type_base[type(node.info).__name__]
            self.type_top.update({type(node.info).__name__: node})
        else: 
            self.type_top[type(node.info).__name__].type_next = node
            node.type_previous = self.type_top[type(node.info).__name__]
            self.type_top.update({type(node.info).__name__: node})
    
    def forward(self, 
                func, 
                parameter,
                restriction = None):
        return_values = []
        if restriction == None:
            next, value = self.base.forward(func, parameter,restriction)
        else: 
            next, value = self.type_base[restriction.__name__].forward(func, parameter,restriction)
        yield value
        while next != None: 
            next, value = next.forward(func,parameter,restriction)
            yield value

    def list(self):
        values = []
        for node in self:
            values.append(node)
        return values

    def __iter__(self, restriction = None):
        return self.forward(getattr, "info", restriction)

    def __getitem__(self,index): 
        return double_linked_list(self.__iter__(index))

if __name__ == "__main__":
    new = double_linked_list([1,"a",2,"b",3,"c",4,"d"])
    new.append('a')
    print(new[int].list())