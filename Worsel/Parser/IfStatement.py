from Statement  import Statement 
from Expression import Expression
from IfComb     import IfComb



class IfStatement (Statement):
    'Take IF statement'

    @property
    def sequence (self):
        return [ 'IF', 
                 Expression,
                 IfComb, 
               ]
    

    