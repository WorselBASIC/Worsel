from Block              import Block
from Kit.Parts.Marker   import Marker
from Kit.Parts.Sequence import Sequence



class ThenMarker    (Marker):
    MARKER = 'THEN'



class ThenSequence  (Sequence):
    'sequence of THEN clause'

    ITEMS = [ ThenMarker,
              Block,
            ]