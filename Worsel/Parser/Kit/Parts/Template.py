from Filter     import Filter
from Associate  import Associate 
from Precedence import Precedence



class Template (Filter):
    'Filter input for expression'

    SEQUENCE   = []
    ASSOCIATE  = Associate 
    PRECEDENCE = Precedence


    def __init__ (self):
        self.position   = 0 
        self.associate  = self.ASSOCIATE.LEFT 
        self.precedence = self.PRECEDENCE.LOWEST

    @property 
    def arity    (self):
        pass

    def __call__ (self, token):
        pass
