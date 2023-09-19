from Kit.Parts.Comb import Comb
from Then           import Then
from Else           import Else
from ThenElse       import ThenElse



class IfComb (Comb):
    'select alternatives of IF statement'
    
    PRECONDITION =   None
    ALTERNATIVES = [ Then,
                     Else, 
                     ThenElse,
                   ]