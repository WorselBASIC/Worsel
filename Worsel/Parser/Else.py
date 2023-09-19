from Kit.Parts.Marker import Marker
from Statement        import Statement 
from Block            import Block



class ElseToken (Marker):
    MARKER = 'ELSE'



class Else      (Statement):
    'capture ELSE statement'
        
    @property
    def sequence (self):
        return [ ElseToken, 
                 Block 
               ]