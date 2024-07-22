#!/usr/bin/python

class node():
    def __init__(self, info):
        self.info = info
        self.next       = None
        self.previous   = None
        self.type_next      = None
        self.type_previous  = None
    
    def forward(self, 
                func, 
                parameter:str,
                restrict:type = None):
        func(getattr(self, parameter))
        if self.next != None:
            self.next.forward(func, parameter, restrict)
class double_linked_list():
    def __init__(self, list:list = []):
        self.length = 0
        self.base = None
        self.top = None
        for layer in list:
            self.append(node(layer))
    
    def append(self, node:node):
        self.length += 1
        if (self.base) == None:
            self.base = node
            return
        elif (self.top == None):
            self.base.next = node
            node.previous = self.base
            self.top = node
        else: 
            self.top.next = node
            node.previous = self.top
            self.top = node
    def forward(self, 
                func, 
                parameter):
        self.base.forward(func, parameter)

    def str(self):
        self.forward(print,"info")

if __name__ == "double_cheeseburger":
    new = double_linked_list([1,2,3,4])
    print("printing")
    new.str()