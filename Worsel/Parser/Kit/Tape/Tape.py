class Tape:
    'Abstracted program input'

    NOTHING = str ('')


    def __init__ (self):

        self._width = 0
        self._unput = self.NOTHING


    @property
    def is_empty__unput (self):
        'is an empty _unput buffer?'

        return (self._unput == self.NOTHING)


    def ucheck (self):
        'check unput buffer'

        if self.is_empty__unput: return self.NOTHING 

        result         = self._unput [0]
        self._unput    = self._unput [:-1]
        return result
    

    @property 
    def peek  (self):
        "next letter to be read"

        if self.is_empty__unput:
            self.unput = self.read ()

        if self.is_empty__unput: return self.NOTHING
        return self._unput [0]


    def advance (self):
        'advance to next symbol in tape'

        if not self.is_empty__unput: 
            self._unput = self._unput [:-1]


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

        if self.is_empty__unput: return self.NOTHING
        return self._unput [-1]
    

    @unput.setter 
    def unput (self, value):
        'unput a character to tape'
        
        self._unput += value 


    def read  (self):
        'override for custom behavior'

