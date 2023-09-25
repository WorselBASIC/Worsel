from Kit.Parts.Sequence                    import Sequence
from Parser.Combs.IfIng.Scans.ThenScan     import Then 
from Parser.Combs.IfIng.Scans.ElseScan     import Else
from Parser.Combs.IfIng.Scans.ThenElseScan import ThenElse 



class IfAlts (Sequence):
    'alternative choices for IF statement'

    ITEMS = [ Then, 
              Else, 
              ThenElse,
            ]

