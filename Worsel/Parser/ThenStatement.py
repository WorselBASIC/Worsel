from Statement      import Statement 
from StatementBlock import StatementBlock


class ThenStatement (Statement):
        
    @property
    def sequence (self):
        return [ 'THEN',
                 StatementBlock,
               ]