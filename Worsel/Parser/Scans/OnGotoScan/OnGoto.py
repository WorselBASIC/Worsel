from Kit.Parts.Filter import Filter 
from OnGotoSequence   import OnGotoSequence



class OnGoto  (Filter):
    'accept ON GOTO statement'

    SEQUENCE = OnGotoSequence
