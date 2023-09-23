from Kit.Parts.Comb import Comb
from IndexedLabel   import IndexedLabel
from NamedLabel     import NamedLabel 
from BlankLabel     import BlankLabel



class LabelComb (Comb):
    'select alternatives of IF statement'
    
    PRECONDITION = None
    ALTERNATIVES = [ IndexedLabel,
                     NamedLabel, 
                     BlankLabel,
                   ]