from Kit.Parts.Marker   import Marker
from Kit.Parts.Sequence import Sequence
from Tokens             import EndOfLineToken



class EndMarker (Marker):
    'Marker beginning END statement'
    
    MARKER = 'END'



class EndSequence (Sequence):
    'accept END statement'

    ITEMS = [ EndMarker, EndOfLineToken ]
