from Parser.Combs.ExpressionIng.Expression import Expression
from Kit.Parts.Sequence                    import Sequence
from Kit.Parts.Marker                      import Marker 
from Tokens                                import EndOfLineToken



class OnMarker (Marker):
    'ON marker for ON GOTO statement'

    MARKER = 'ON'
    


class GotoMarker (Marker):
    'GOTO marker for ON GOTO statement'

    MARKER = 'GOTO'



class OnGotoSequence (Sequence):
    'sequence of ON GOTO statement'

    ITEMS = [ OnMarker,
              Expression,
              GotoMarker,
              Expression,
              EndOfLineToken,
            ]