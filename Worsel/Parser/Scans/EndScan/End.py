from Kit.Parts.Filter                 import Filter
from Parser.Scans.EndScan.EndSequence import EndSequence



class End       (Filter):
    'accept END statement'

    SEQUENCE = EndSequence

