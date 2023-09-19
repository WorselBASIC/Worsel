from Expression import Expression 



class Dyad (Expression):

    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER, Expression ]