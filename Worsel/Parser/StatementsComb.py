

from Kit.Parts.Comb  import Comb
from Let             import Let 
from Option          import Option
from End             import End 
from Stop            import Stop 
from Rem             import Rem 
from Goto            import Goto 
from OnGoto          import OnGoto
from If              import If 



class StatementsComb (Comb):
    'Comb from choice of statements'

    PRECONDITION =   None

    ALTERNATIVES = [ Let,
                     Option,
                     Stop,
                     Rem,
                     Goto,
                     OnGoto
                     If,
                   ]