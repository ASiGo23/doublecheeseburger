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
        value = func(self, parameter)
        return(self.next, value)
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
                parameter:str):
        return_values = []
        next, value = self.base.forward(func, parameter)
        return_values.append(value)
        while next != None: 
            next, value = next.forward(func,parameter)
            return_values.append(value)
        return return_values

    def list(self):
        return self.forward(getattr,"info")

if __name__ == "__main__":
    new = double_linked_list([1,2,3,4])
    print(new.list())