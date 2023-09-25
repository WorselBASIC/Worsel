from Kit.Parts.Sequence                             import Sequence
from Parser.Combs.IfIng.Scans.ThenScan.Then         import Then 
from Parser.Combs.IfIng.Scans.ElseScan.Else         import Else
from Parser.Combs.IfIng.Scans.ThenElseScan.ThenElse import ThenElse 



class IfAlts (Sequence):
    'alternative choices for IF statement'

    ITEMS = [ Then, 
              Else, 
              ThenElse,
            ]

