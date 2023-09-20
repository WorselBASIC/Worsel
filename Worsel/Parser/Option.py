from Statement        import Statement 
from Expression       import Expression
from Tokens           import EndOfLineToken
from Kit.Parts.Marker import Marker



class OptionMarker    (Marker):
    'marker for OPTION statement'
    
    MARKER = 'OPTION'



class Option (Statement):

    @property
    def sequence (self):
        return [ OptionMarker,
                 Expression,
                 Expression,
                 EndOfLineToken
               ]