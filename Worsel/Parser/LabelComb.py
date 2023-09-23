from Kit.Parts.Comb import Comb
from IndexedLabel   import IndexedLabel
from NamedLabel     import NamedLabel 
from BlankLabel     import BlankLabel


class LabelAlts (list):
    'alternative choices for statement label'

    def __init__ (self):
        list.__init__ (self, [ IndexedLabel,
                               NamedLabel, 
                               BlankLabel,
                             ])



class LabelComb (Comb):
    'select alternatives of statement label'
    
    PRECONDITION = None
    ALTERNATIVES = LabelAlts

    def __init__ (self):
        Comb.__init__ (self)