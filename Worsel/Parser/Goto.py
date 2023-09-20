from Kit.Parts.Marker import Marker
from Statement        import Statement 
from Tokens           import EndOfLineToken
from Expression       import Expression



class GotoMarker    (Marker):
    'marker for GOTO statement'
    
    MARKER = 'GOTO'



class Goto          (Statement):
    'accept GOTO statement'

    @property
    def sequence (self):
        return [ GotoMarker,
                 Expression,
                 EndOfLineToken,
               ]