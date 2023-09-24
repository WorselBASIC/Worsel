from Kit.Parts.Marker                    import Marker
from Parser.Combs.StatementIng.Statement import Statement 
from Block                               import Block



class ElseToken (Marker):
    MARKER = 'ELSE'



class Else      (Statement):
    'capture ELSE statement'
        
    @property
    def sequence (self):
        return [ ElseToken, 
                 Block 
               ]