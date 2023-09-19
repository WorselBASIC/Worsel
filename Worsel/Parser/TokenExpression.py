from Expression import Expression 



class TokenExpression (Expression):

    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER ]