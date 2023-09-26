from collections import deque



class Stack:
    "wrapper around platform's stack"


    def __init__ (self):
        self._data = deque ()


    @property 
    def front     (self):
        'get front of stack'

        return self._data [0] 
    

    @front.setter
    def front    (self, value):
        'use assignment to front as push/pop'

        if (value == None):
            #AJF: need balance check here
            self._data.popleft ()
        else:
            self._data.appendleft (value)


    @property 
    def rear     (self):
        'get rear of stack'

        return self._data [-1] 
    