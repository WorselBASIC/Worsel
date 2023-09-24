from Kit.Parts.Filter import Filter 
from StopSequence     import StopSequence



class Stop (Filter):
    'accept STOP statement'

    SEQUENCE = StopSequence