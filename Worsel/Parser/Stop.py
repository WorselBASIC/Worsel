from Kit.Parts.Marker                    import Marker
from Parser.Combs.StatementIng.Statement import Statement 
from Tokens                              import EndOfLineToken



class StopMarker (Marker):
    MARKER = 'STOP'



class Stop (Statement):
    @property
    def sequence (self):
        return [ StopMarker,
                 EndOfLineToken
               ]