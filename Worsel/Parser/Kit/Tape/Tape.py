class Tape:
    'Abstract interface to program input'

    def __init__ (self):
        self._next  = None
        self._width = 0

    @property
    def next  (self):
        return self._next

    @property
    def width (self):
        return self._width
    
    @width.setter
    def width (self, wide):
        self._width = wide


