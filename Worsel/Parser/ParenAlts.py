from Kit.Parts.Sequence   import Sequence 
from Tokens               import RParenToken
from Kit.Parts.Expression import Expression



class ParenAlts (Sequence):
    ITEMS = [ Expression, RParenToken]