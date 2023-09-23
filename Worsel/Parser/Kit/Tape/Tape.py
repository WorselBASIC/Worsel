class Tape:
    'Abstract interface to program input'

    def __init__ (self):
        self._next  = None
        self._width = 0
        self._unput = []


    @property
    def _ucheck (self):
        'check unput buffer'

        if self._unput == []:
            return None
        
        result      = self._unput []
        self._unput = self._unput [:-1]
        return result


    @property
    def next  (self):
        'next character from tape'

        result     = self._ucheck 
        if result != None: return result
        return self._next
        

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



