from Statement        import Statement 
from Block            import Block
from Kit.Parts.Marker import Marker



class ThenMarker    (Marker):
    MARKER = 'THEN'



class ThenStatement (Statement):
        
    @property
    def sequence (self):
        return [ ThenMarker,
                 Block,
               ]