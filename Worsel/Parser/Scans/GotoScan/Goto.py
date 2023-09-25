from Kit.Parts.Filter                   import Filter 
from Parser.Scans.GotoScan.GotoSequence import GotoSequence



class Goto (Filter):
    'accept GOTO statement'

    SEQUENCE = GotoSequence
