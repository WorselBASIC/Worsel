from Kit.Parts.Filter                 import Filter
from Parser.Scans.RemScan.RemSequence import RemSequence



class Rem (Filter):
    'accept REM statement'

    SEQUENCE = RemSequence
