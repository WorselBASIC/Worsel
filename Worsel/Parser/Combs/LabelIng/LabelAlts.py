from Kit.Parts.Sequence import Sequence
from IndexedLabel       import IndexedLabel
from NamedLabel         import NamedLabel 
from BlankLabel         import BlankLabel



class LabelAlts (Sequence):
    'alternative choices for statement label'

    ITEMS = [ IndexedLabel,
              NamedLabel, 
              BlankLabel,
            ]
