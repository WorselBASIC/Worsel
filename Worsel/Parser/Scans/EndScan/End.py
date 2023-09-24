from Kit.Parts.Filter import Filter
from EndSequence      import EndSequence



class End       (Filter):
    'accept END statement'

    SEQUENCE = EndSequence

