from Kit.Parts.Marker                      import Marker 
from Kit.Parts.Sequence                    import Sequence
from Parser.Combs.ExpressionIng.Expression import Expression 
from Parser.Combs.IfIng.IfComb             import IfComb



class IfMarker   (Marker):
    MARKER = 'IF'



class IfSequence (Sequence):
    'sequence of IF statement'

    ITEMS = [ IfMarker, 
              Expression,
              IfComb, 
            ]
    

    