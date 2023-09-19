from Comb            import Comb 
from ParenExpression import ParenExpression
from Expression      import Expression


class ParenComb (Comb):

    PRECONDITION =   None
    ALTERNATIVES = [ Expression, ParenExpression ]