from Parser.Combs.ExpressionIng.Expression import Expression
from Tokens                                import EndOfLineToken
from Kit.Parts.Marker                      import Marker
from Kit.Parts.Sequence                    import Sequence


class OptionMarker    (Marker):
    'marker for OPTION statement'
    
    MARKER = 'OPTION'



class OptionSequence  (Sequence):

    ITEMS = [ OptionMarker,
              Expression,
              Expression,
              EndOfLineToken
            ]