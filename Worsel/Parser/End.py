from Kit.Parts.Marker import Marker
from Statement        import Statement
from Tokens           import EndOfLineToken



class EndMarker (Marker):
    MARKER = 'END'



class End (Statement):
    @property
    def sequence (self):
        return [ EndMarker,
                 EndOfLineToken
               ]
