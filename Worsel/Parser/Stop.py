from Kit.Parts.Marker import Marker
from Statement        import Statement
from Tokens           import EndOfLineToken



class StopMarker (Marker):
    MARKER = 'STOP'



class Stop (Statement):
    @property
    def sequence (self):
        return [ StopMarker,
                 EndOfLineToken
               ]