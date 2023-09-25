from Kit.Parts.Filter                               import Filter
from Parser.Combs.IfIng.Scans.ElseScan.ElseSequence import ElseSequence



class Else      (Filter):
    'capture ELSE statement'
        
    SEQUENCE = ElseSequence
    