class circularQueue(object):
    def __init__(self, size):
        self.__size = size
        self.__queue = [None]*size
        self.__head = 0
        self.__tail = 0

    def enqueue(self, item):
        print("TAIL", self.__tail)
        if not(self.__isBefore()):
            self.__queue[self.__tail] = item
            self.__updateTail()
        else:
            raise QueueError("Queue full")

    def dequeue(self):
        if not(self.__isEmpty()):
            item = self.__queue[self.__head]
            self.__updateHead()
            return item
        else:
            raise QueueError("Empty Queue")
        
    def __isBefore(self):
        return( self.__head - self.__tail == 1 or (self.__head == 0 and self.__tail == self.__size-1))

    def __updateTail(self):
       self.__tail += 1
       if self.__tail >= self.__size:
           self.__tail = 0

    def __updateHead(self):
        self.__head += 1
        if self.__head >= self.__size:
            self.__head = 0

    def __isEmpty(self):
        return (self.__head == self.__tail)

    def display(self):
        p = self.__head
        while p != self.__tail:
            print(p, self.__queue[p])
            p+= 1
            if p >= self.__size:
                p = 0


class QueueError(Exception):
    def __init__(self, message):
        self.__message = message
    def toString(self):
        return (self.__message)

    
    
