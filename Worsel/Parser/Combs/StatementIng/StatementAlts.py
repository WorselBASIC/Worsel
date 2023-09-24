from Kit.Parts.Sequence   import Sequence
from Parser.Combs.IfIng   import If
from Let                  import Let 
from Option               import Option
from Parser.Scans.EndScan import End
from Stop                 import Stop 
from Rem                  import Rem 
from Goto                 import Goto 
from OnGoto               import OnGoto



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