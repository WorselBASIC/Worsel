from Kit.Parts.Comb            import Comb
from Parser.Combs.IfIng.IfAlts import IfAlts



class IfComb (Comb):
    'select alternatives of IF statement'
    
    PRECONDITION = None
    ALTERNATIVES = IfAlts