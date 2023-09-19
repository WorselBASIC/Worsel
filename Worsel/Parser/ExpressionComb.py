from Comb                     import Comb 
from Expression               import Expression
from AdditionExpression       import AdditionExpression
from SubtractionExpression    import SubtractionExpression
from MultiplicationExpression import MultiplicationExpression
from DivisionExpression       import DivisionExpression
from SequenceExpression       import SequenceExpression
from GreaterEqualExpression   import GreaterEqualExpression
from GreaterThanExpression    import GreaterThanExpression
from LessEqualExpression      import LessEqualExpression
from LessThanExpression       import LessThanExpression
from NotEqualExpression       import NotEqualExpression



class ExpressionComb (Comb):
    PRECONDITION =   Expression 

    ALTERNATIVES = [ AdditionExpression,
                     SubtractionExpression, 
                     MultiplicationExpression,
                     DivisionExpression,
                     SequenceExpression,
                     GreaterEqualExpression, 
                     GreaterThanExpression, 
                     LessEqualExpression, 
                     LessThanExpression, 
                     NotEqualExpression,
                   ]
