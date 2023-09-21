"""
" This file uses these libraries:
"""
from Statement import Statement 
from Comb      import Comb



class Block (Statement):
    'take block of statements'

    COMB = Comb 


    def __init__ (self, _tape):
        self.comb = self.COMB ()
        self.tape = _tape


    def __call__ (self):
        while (datum := self.tape.next):
            if (status := self.comb (datum)):
                return self.complain (self.comb, status, datum)
            


""" End of Block.py """