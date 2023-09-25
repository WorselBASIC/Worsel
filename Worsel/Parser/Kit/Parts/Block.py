"""
" This file uses these libraries:
"""
from Kit.Tape.TheTape import get_the_tape
from Statement        import Statement 
from Comb             import Comb



class Block (Statement):
    'take block of statements'

    COMB = Comb 


    def __init__ (self):
        self.comb = self.COMB ()


    def __call__ (self):
        tape = get_the_tape ()
        while (datum := tape.next):
            self.tape.unput = datum
            if (status := self.comb  (tape)):
                return self.complain (self.comb, status, datum)
            


""" End of Block.py """