"""
" This file uses these libraries:
"""
from Worsel.Parser.Kit.Tape.TheTape import TheTape
from Statement                      import Statement 
from Comb                           import Comb



class Block (Statement):
    'parse block of statements'

    COMB = Comb 


    def __init__ (self):

        self.comb       = None 
        if (self.COMB  == None): return
        self.comb       = self.COMB ()


    def __call__ (self):
        'parse action'

        tape = TheTape ().tape  # singleton
        
        while (datum := tape.peek):
            if (status := self.comb  ()):
                return self.complain (self.comb, status, datum)
            


""" End of Block.py """