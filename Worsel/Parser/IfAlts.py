from Kit.Parts.Sequence import Sequence
from Then               import Then
from Else               import Else
from ThenElse           import ThenElse



class IfAlts (Sequence):
    'alternative choices for IF statement'

    ITEMS = [Then, Else, ThenElse]
