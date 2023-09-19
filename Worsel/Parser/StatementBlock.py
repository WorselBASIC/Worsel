"""
" This file uses these libraries:
"""
from Statement     import Statement 
from StatementComb import StatementComb



class StatementBlock (Statement):
    'take block of statements'

    def __init__ (self):
        self.comb = StatementComb () 

    def __call__ (self, tape):
        while (datum := tape.next):
            if (status := self.comb (datum)):
                return self.complain (self.comb, status, datum)
            


""" End of StatementBlock.py """