from Kit.Parts.Marker           import Marker
from Kit.Parts.Sequence         import Sequence
from Parser.Combs.ExpressionIng import Expression
from Tokens                     import EndOfLineToken



class GotoMarker    (Marker):
    'marker for GOTO statement'
    
    MARKER = 'GOTO'



class GotoSequence  (Sequence):
    'accept GOTO statement'

    SEQUENCE = [ GotoMarker,
                 Expression,
                 EndOfLineToken,
               ]