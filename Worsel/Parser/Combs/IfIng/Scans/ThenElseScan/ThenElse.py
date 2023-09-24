from Parser.Combs.StatementIng.Statement import Statement 
from Block                               import Block
from Kit.Parts.Marker                    import Marker



class ThenMarker (Marker):
    MARKER = 'THEN'



class ElseMarker (Marker):
    MARKER = 'ELSE'    



class ThenElse (Statement):
        
    @property
    def sequence (self):
        return [ ThenMarker,
                 Block,
                 ElseMarker,
                 Block,
               ]