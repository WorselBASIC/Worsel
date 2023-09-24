

from Kit.Parts.Comb                  import Comb
from Parser.Combs.LabelIng.LabelComb import LabelComb
from StatementAlts                   import StatementAlts



class StatementsComb (Comb):
    'Comb from choice of statements'

    PRECONDITION = LabelComb
    ALTERNATIVES = StatementAlts