from Expression import Expression 



class Enclosed (Expression):

    LHS    = None
    CENTER = None
    RHS    = None
    
    @property
    def sequence (self):
        return [ self.LHS,
                 self.CENTER, 
                 self.RHS,
               ]