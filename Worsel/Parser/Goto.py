from Kit.Parts.Marker import Marker
from Statement        import Statement 
from Tokens           import EndOfLineToken
from Expression       import Expression



class GotoMarker    (Marker):
    MARKER = 'GOTO'



class GotoStatement (Statement):

    @property
    def sequence (self):
        return [ GotoMarker,
                 Expression,
                 EndOfLineToken,
               ]