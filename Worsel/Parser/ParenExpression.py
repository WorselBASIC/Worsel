from Expression import Expression



class ParenExpression (Expression):

    LMARKER = '('
    RMARKER = ')'
    
    @property
    def sequence (self):
        return [ self.LMARKER, 
                 Expression, 
                 self.RMARKER 
               ]