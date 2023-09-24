from Kit.Parts.Marker   import Marker
from Tokens             import EndOfLineToken
from Kit.Parts.Sequence import Sequence



class RemMarker (Marker):
    MARKER = 'REM'



class Comment:
    pass



class RemSequence (Sequence):
    ITEMS = [ RemMarker,
              Comment,
              EndOfLineToken,
            ]

