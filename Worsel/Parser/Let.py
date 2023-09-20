from Kit.Parts.Token  import Token
from Kit.Parts.Marker import Marker
from Statement        import Statement 
from Expression       import Expression
from Tokens           import EndOfLineToken



class LetMarker   (Marker):
    MARKER = 'LET'


class AssignToken (Token):
    MARKER = '='



class LValue:
    'accept an assignable value'


class Let (Statement):
    'accept a LET statement'

    @property
    def sequence (self):
        return [ LetMarker,
                 LValue,
                 AssignToken,
                 Expression,
                 EndOfLineToken,
               ]