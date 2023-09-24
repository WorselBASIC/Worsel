from Kit.Parts.Comb import Comb 
from ParenAlts      import ParenAlts



class ParenComb (Comb):
    'Comb through optional parentheses'
    
    PRECONDITION = None
    ALTERNATIVES = ParenAlts