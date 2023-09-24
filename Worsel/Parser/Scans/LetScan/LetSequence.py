from Kit.Parts.Token                       import Token
from Kit.Parts.Marker                      import Marker
from Kit.Parts.Sequence                    import Sequence
from Parser.Combs.ExpressionIng.Expression import Expression
from Tokens                                import EndOfLineToken



class LetMarker   (Marker):
    MARKER = 'LET'


class AssignToken (Token):
    MARKER = '='



class LValue:
    'accept an assignable value'


class LetSequence (Sequence):
    'sequence of a LET statement'

    ITEMS = [ LetMarker,
              LValue,
              AssignToken,
              Expression,
              EndOfLineToken,
            ]