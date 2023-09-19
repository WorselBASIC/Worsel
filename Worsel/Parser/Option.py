from Statement        import Statement 
from Expression       import Expression
from Tokens           import EndOfLineToken
from Kit.Parts.Marker import Marker



class OptionMarker    (Marker):
    MARKER = 'OPTION'



class OptionStatement (Statement):

    @property
    def sequence (self):
        return [ OptionMarker,
                 Expression,
                 Expression,
                 EndOfLineToken
               ]