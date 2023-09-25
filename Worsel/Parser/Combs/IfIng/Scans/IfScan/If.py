from Kit.Parts.Filter                           import Filter
from Parser.Combs.IfIng.Scans.IfScan.IfSequence import IfSequence



class If (Filter):
    'accept IF statement'

    SEQUENCE = IfSequence

    

    