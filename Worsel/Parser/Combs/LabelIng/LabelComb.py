from Kit.Parts.Comb                  import Comb
from Parser.Combs.LabelIng.LabelAlts import LabelAlts



class LabelComb (Comb):
    'select alternatives of statement label'
    
    PRECONDITION = None
    ALTERNATIVES = LabelAlts
