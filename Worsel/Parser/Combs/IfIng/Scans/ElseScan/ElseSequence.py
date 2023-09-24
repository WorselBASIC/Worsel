from Kit.Parts.Marker   import Marker
from Block              import Block
from Kit.Parts.Sequence import Sequence



class ElseToken    (Marker):
    MARKER = 'ELSE'



class ElseSequence (Sequence):
    'sequence of ELSE statement'

    ITEMS = [ ElseToken, Block ]