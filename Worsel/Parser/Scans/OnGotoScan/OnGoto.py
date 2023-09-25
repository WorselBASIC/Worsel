from Kit.Parts.Filter                       import Filter 
from Parser.Scans.OnGotoScan.OnGotoSequence import OnGotoSequence



class OnGoto  (Filter):
    'accept ON GOTO statement'

    SEQUENCE = OnGotoSequence
