from arrayLib import * ## Requires the Array Library

class Stack(object):
  
    def __init__(self, size):
        self._pile = Array(size)
        self._size = size
        self._topOfStack = 0
        
    def __isFull(self):
        return self._topOfStack == self.__maxSize()
        
    def isEmpty(self):
        return self._topOfStack == 0
        
    def __maxSize(self):
        return self._size
        
    def push(self, item):
        if not(self.__isFull()):
            self._pile.assign(self._topOfStack, item)
            self._topOfStack+=1
        else:
            raise StackException('Stack overflow error')
        
    def pop(self):
        if not(self.isEmpty()):
            self._topOfStack-=1
            item = self._pile.get(self._topOfStack)
            return item
        else:
            raise StackException('Stack empty error')

class StackException(Exception):
    
    def __init__(self, value):
        self._value = value
    
    def __str__(self):
        return self._value
       
