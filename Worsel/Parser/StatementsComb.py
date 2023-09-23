

from Kit.Parts.Comb  import Comb
from LabelComb       import LabelComb
from Let             import Let 
from Option          import Option
from End             import End 
from Stop            import Stop 
from Rem             import Rem 
from Goto            import Goto 
from OnGoto          import OnGoto
from If              import If 


class StatementAlts (list):
    'alternative choices for IF statement'

    def __init__ (self):
        list.__init__ (self, [ Let,
                               Option,
                               Stop,
                               End,
                               Rem,
                               Goto,
                               OnGoto,
                               If,
                             ])



class StatementsComb (Comb):
    'Comb from choice of statements'

    PRECONDITION = LabelComb
    ALTERNATIVES = StatementAlts