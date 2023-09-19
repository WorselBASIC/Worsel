from Statement      import Statement 
from StatementBlock import StatementBlock



class ThenElseStatement (Statement):
        
    @property
    def sequence (self):
        return [ 'THEN',
                 StatementBlock,
                 'ELSE',
                 StatementBlock,
               ]