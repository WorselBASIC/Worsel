"""
" This file uses the following libraries:
"""
from Kit.Stack.Stack                import Stack
from Worsel.Parser.Kit.Tape.TheTape import TheTape
from Sequence                       import Sequence
from Complaint                      import Complaint



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


    @property 
    def is_acceptable   (self):
        'may we begin parse with this sequence?'

        tape  = TheTape().tape

        return (tape.peek == self.starting)


    def __call__        (self, datum):
        Stack.put       (self, datum)
