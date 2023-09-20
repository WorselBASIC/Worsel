from Expression import Expression 



class Token (Expression):
    'Accept an expression composed of a single marker'

    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER ]