"""
" This file uses these libraries:
"""
from Statement import Statement 
from Comb      import Comb
from Tape.Tape import Tape



class Block (Statement):
    'take block of statements'

    COMB = Comb 

    def __init__ (self):
        self.comb = self.COMB ()

    def __call__ (self):
        while (datum := Tape.next):
            if (status := self.comb (datum)):
                return self.complain (self.comb, status, datum)
            


""" End of Block.py """