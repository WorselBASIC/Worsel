from Kit.Parts.Comb       import Comb 
from Tokens               import RParenToken
from Kit.Parts.Expression import Expression


class ParenComb (Comb):
    ''
    
    PRECONDITION =   None
    ALTERNATIVES = [ Expression, RParenToken ]