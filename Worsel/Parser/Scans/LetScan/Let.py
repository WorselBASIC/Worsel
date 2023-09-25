from Kit.Parts.Filter                 import Filter 
from Parser.Scans.LetScan.LetSequence import LetSequence



class Let (Filter):
    'accept a LET statement'

    SEQUENCE = LetSequence