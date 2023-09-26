from collections import deque



class Stack:
    "wrapper around platform's stack"


    def __init__ (self):
        self._data = deque ()


    @property 
    def front       (self):
        'get front of stack'

        if (len (self) == 0): return None
        return self._data [0] 
    

    @front.setter
    def front      (self, value):
        'use assignment to front as push/pop'

        if (value == None):
            #AJF: need balance check here
            self._data.popleft ()
        else:
            self._data.appendleft (value)


    @property 
    def rear       (self):
        'get rear of stack'

        if (len (self) == 0): return None
        return self._data [-1] 
    

    def __len__    (self):
        return len (self._data)