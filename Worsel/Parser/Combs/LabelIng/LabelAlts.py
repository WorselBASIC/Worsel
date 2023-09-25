from Kit.Parts.Sequence                 import Sequence
from Parser.Combs.LabelIng.IndexedLabel import IndexedLabel
from Parser.Combs.LabelIng.NamedLabel   import NamedLabel 
from Parser.Combs.LabelIng.BlankLabel   import BlankLabel



class LabelAlts (Sequence):
    'alternative choices for statement label'

    ITEMS = [ IndexedLabel,
              NamedLabel, 
              BlankLabel,
            ]
