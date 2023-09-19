from Comb import Comb
from ThenStatement     import ThenStatement 
from ElseStatement     import ElseStatement 
from ThenElseStatement import ThenElseStatement



class IfComb (Comb):
    PRECONDITION =   None

    ALTERNATIVES = [ ThenStatement,
                     ElseStatement, 
                     ThenElseStatement,
                   ]