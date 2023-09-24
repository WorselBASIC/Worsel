from Kit.Parts.Marker                      import Marker 
from Parser.Combs.StatementIng.Statement   import Statement 
from Parser.Combs.ExpressionIng.Expression import Statement 
from IfComb                                import IfComb



class IfMarker (Marker):
    MARKER = 'IF'



class If       (Statement):
    'accept IF statement'

    @property
    def sequence (self):
        return [ IfMarker, 
                 Expression,
                 IfComb, 
               ]
    

    