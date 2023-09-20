from Statement import Statement 



class Marker (Statement):
    'accept a statement composed of a single marker'
    
    MARKER = None
    
    @property
    def sequence (self):
        return [ self.MARKER ]