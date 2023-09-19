from Statement      import Statement 
from StatementBlock import StatementBlock


class ElseStatement (Statement):
        
    @property
    def sequence (self):
        return [ 'ELSE',
                 StatementBlock,
               ]