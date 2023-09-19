from Statement        import Statement 
from Kit.Parts.Marker import Marker 
from Tokens           import EndOfLineToken
from Expression       import Expression



class OnMarker (Marker):
    MARKER = 'ON'
    


class GotoMarker (Marker):
    MARKER = 'GOTO'



class OnGotoStatement (Statement):

    @property
    def sequence (self):
        return [ OnMarker,
                 Expression,
                 GotoMarker,
                 Expression,
                 EndOfLineToken,
               ]