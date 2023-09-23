from Kit.Parts.Comb import Comb
from Then           import Then
from Else           import Else
from ThenElse       import ThenElse



class IfAlts (list):
    'alternative choices for IF statement'

    def __init__ (self):
        list.__init__ ([Then,
                        Else, 
                        ThenElse,])


class IfComb (Comb):
    'select alternatives of IF statement'
    
    PRECONDITION = None
    ALTERNATIVES = IfAlts