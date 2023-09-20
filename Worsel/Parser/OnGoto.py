from Statement        import Statement 
from Kit.Parts.Marker import Marker 
from Tokens           import EndOfLineToken
from Expression       import Expression



class OnMarker (Marker):
    'ON marker for ON GOTO statement'

    MARKER = 'ON'
    


class GotoMarker (Marker):
    'GOTO marker for ON GOTO statement'

    MARKER = 'GOTO'



class OnGoto      (Statement):
    'accept ON GOTO statement'

    @property
    def sequence (self):
        return [ OnMarker,
                 Expression,
                 GotoMarker,
                 Expression,
                 EndOfLineToken,
               ]