from Statement  import Statement 
from Expression import Expression



class LetStatement (Statement):

    @property
    def sequence (self):
        return [ 'LET',
                 LValue,
                 '='
                 Expression
                 EndOfLine
               ]