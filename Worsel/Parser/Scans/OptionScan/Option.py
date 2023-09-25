from Kit.Parts.Filter                       import Filter 
from Parser.Scans.OptionScan.OptionSequence import OptionSequence



class Option (Filter):
    'filter to accept OPTION statement'

    SEQUENCE = OptionSequence