from Statement        import Statement 
from Kit.Parts.Marker import Marker
from Tokens           import EndOfLineToken



class RemMarker (Marker):
    MARKER = 'REM'



class Comment:
    pass



class Rem       (Statement):
    @property
    def sequence (self):
        return [ RemMarker,
                 Comment,
                 EndOfLineToken,
               ]

