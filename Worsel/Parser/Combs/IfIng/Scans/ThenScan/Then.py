from Kit.Parts.Filter                               import Filter 
from Parser.Combs.IfIng.Scans.ThenScan.ThenSequence import ThenSequence



class Then (Filter):
    'accept THEN clause'

    SEQUENCE = ThenSequence
        
