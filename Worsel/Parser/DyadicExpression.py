from Expression import Expression 



class DyadicExpression (Expression):

    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER, Expression ]