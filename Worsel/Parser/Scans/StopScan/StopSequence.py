from Kit.Parts.Marker   import Marker
from Tokens             import EndOfLineToken
from Kit.Parts.Sequence import Sequence



class StopMarker (Marker):
    MARKER = 'STOP'



class StopSequence (Sequence):
    'sequence of STOP statement'
    
    ITEMS = [ StopMarker,
              EndOfLineToken
            ]