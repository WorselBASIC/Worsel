"""
" This file uses the following libraries:
"""
from Worsel.Parser.Kit.Stack.TheStack import TheStack
from Worsel.Parser.Kit.Tape.TheTape   import TheTape
from Sequence                         import Sequence
from Complaint                        import Complaint



class Filter:
    'contains parsing primitives'

    SEQUENCE = Sequence


    def __init__        (self):

        self.index     = 0 
        self.is_in_use = False
        self.complaint = Complaint ()
        self._sequence = self.SEQUENCE ()


    @property 
    def sequence        (self):
        'the sequence of items being filtered'

        return self._sequence
    

    @property 
    def starting        (self):
        'override for custom behavior'

        if (len (self.sequence) == 0):
            return None
        
        begin = self.sequence [0]
        return begin


    def is_front_check  (self, peek, check):
        'override for custom behavior'

        return False 
    

    @property 
    def is_acceptable   (self):
        'may we begin parse with this sequence?'

        return self.is_front_check (self.me.front, 
                                    self.starting)

    @property 
    def me              (self):
        return TheStack ().stack
    

    @me.setter 
    def me              (self, value):
        TheStack ().stack = value


