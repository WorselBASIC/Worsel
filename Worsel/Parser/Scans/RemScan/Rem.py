from Kit.Parts.Filter import Filter
from RemSequence      import RemSequence



class Rem (Filter):
    'accept REM statement'

    SEQUENCE = RemSequence
