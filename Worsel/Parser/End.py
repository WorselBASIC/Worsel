from Kit.Parts.Marker import Marker
from Statement        import Statement
from Tokens           import EndOfLineToken



class EndMarker (Marker):
    'Marker beginning END statement'
    
    MARKER = 'END'



class End       (Statement):
    'accept END statement'

    @property
    def sequence (self):
        return [ EndMarker,
                 EndOfLineToken
               ]
