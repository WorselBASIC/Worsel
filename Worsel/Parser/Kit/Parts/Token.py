from Expression import Expression 



class Token (Expression):

    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER ]