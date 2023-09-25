class Sequence (list):
    'overrideable list object, possibly empty'

    ITEMS = []


    def __init__      (self):

        klasses   = [ i   for i in self.ITEMS ]
        instances = [ i() for i in klasses]
        list.__init__ (self, instances)