from Statement  import Statement 
from Expression import Expression
from EndOfLine  import EndOfLine



class OptionStatement (Statement):

    @property
    def sequence (self):
        return [ 'OPTION',
                 Expression,
                 Expression,
                 EndOfLine
               ]