from Statement import Statement 



class Marker (Statement):
    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER ]