from Kit.Parts.Comb import Comb
from Expression     import Expression

from Dyads          import AdditionDyad 
from Dyads          import SubtractionDyad 
from Dyads          import MultiplicationDyad 
from Dyads          import DivisionDyad 
from Dyads          import SequenceDyad 
from Dyads          import GEDyad 
from Dyads          import GTDyad 
from Dyads          import LTDyad 
from Dyads          import LEDyad 
from Dyads          import NEDyad
from Dyads          import EQDyad


class ExpressionAlts (list):
    'alternative choices for expression'

    def __init__ (self):
        list.__init__ ( [ AdditionDyad,
                          SubtractionDyad, 
                          MultiplicationDyad,
                          DivisionDyad,
                          SequenceDyad,
                          GEDyad,
                          GTDyad,
                          LEDyad,
                          LTDyad,
                          NEDyad,
                          EQDyad,
                        ])


class ExpressionComb (Comb):
    'Comb for BASIC Expression'
    
    PRECONDITION = Expression 
    ALTERNATIVES = ExpressionAlts
