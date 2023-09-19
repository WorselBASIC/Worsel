from Comb            import Comb
from LetStatement    import LetStatement 
from OptionStatement import OptionStatement
from EndStatement    import EndStatement 
from StopStatement   import StopStatement
from RemStatement    import RemStatement
from GotoStatement   import GotoStatement 
from OnGotoStatement import OnGotoStatement
from IfStatement     import IfStatement



class StatementComb (Comb):
    'Comb from choice of statements'

    PRECONDITION =   None

    ALTERNATIVES = [ LetStatement,
                     OptionStatement,
                     EndStatement,
                     StopStatement,
                     RemStatement,
                     GotoStatement,
                     OnGotoStatement,
                     IfStatement,
                   ]