from Kit.Parts.Marker import Marker 
from Statement        import Statement 
from Expression       import Expression
from IfComb           import IfComb



class IfMarker (Marker):
    MARKER = 'IF'



class If       (Statement):
    'Take IF statement'

    @property
    def sequence (self):
        return [ IfMarker, 
                 Expression,
                 IfComb, 
               ]
    

    