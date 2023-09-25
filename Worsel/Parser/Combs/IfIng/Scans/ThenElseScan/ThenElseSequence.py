from Kit.Parts.Sequence import Sequence
from Parser.ParserBlock import ParserBlock
from Kit.Parts.Marker   import Marker



class ThenMarker (Marker):
    MARKER = 'THEN'



class ElseMarker (Marker):
    MARKER = 'ELSE'    



class ThenElseSequence (Sequence):
    'sequence of THEN ELSE clause'

    ITEMS = [ ThenMarker,
              ParserBlock,
              ElseMarker,
              ParserBlock,
            ]