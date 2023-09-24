from Kit.Parts.Sequence import Sequence
from Let                import Let 
from Option             import Option
from End                import End 
from Stop               import Stop 
from Rem                import Rem 
from Goto               import Goto 
from OnGoto             import OnGoto
from If                 import If 



class StatementAlts (Sequence):
    'alternative choices for IF statement'

    ITEMS = [ Let,
              Option,
              Stop,
              End,
              Rem,
              Goto,
              OnGoto,
              If,
            ]