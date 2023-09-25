from Kit.Parts.Marker   import Marker
from Parser.ParserBlock import ParserBlock
from Kit.Parts.Sequence import Sequence



class ElseToken    (Marker):
    MARKER = 'ELSE'



class ElseSequence (Sequence):
    'sequence of ELSE statement'

    ITEMS = [ ElseToken, 
              ParserBlock 
            ]