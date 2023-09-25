class Tape:
    'Abstracted program input'


    def __init__ (self):

        self._width = 0
        self._unput = []


    def ucheck (self):
        'check unput buffer'

        if self._unput == []: return None 
        result         = self._unput [0]
        self._unput    = self._unput [:-1]
        return result
    

    @property 
    def peek  (self):
        "next letter to be read"

        if self._unput == []:
            self.unput =  self.read ()

        return self.unput [0]


    @property
    def width (self):
        'width of tape in bytes'

        return self._width
    

    @width.setter
    def width (self, wide):
        'set width of tape in bytes'

        self._width = wide


    @property
    def unput (self):
        'latest character unput to this tape'

        if (self._unput == None): return None
        return self._unput [-1]
    

    @unput.setter 
    def unput (self, value):
        'unput a character to tape'
        
        self._unput += [ value ]


    def read  (self):
        'override for custom behavior'

