from Kit.Parts.Filter                   import Filter 
from Parser.Scans.StopScan.StopSequence import StopSequence



class Stop (Filter):
    'accept STOP statement'

    SEQUENCE = StopSequence