from Kit.Parts.Comb     import Comb
from Expression         import Expression
from ExpressionAlts     import ExpressionAlts



class ExpressionComb (Comb):
    'Comb for BASIC Expression'
    
    PRECONDITION = Expression 
    ALTERNATIVES = ExpressionAlts
