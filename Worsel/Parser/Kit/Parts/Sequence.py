class Sequence (list):
    'overrideable list object, possibly empty'

    ITEMS = []


    def __init__      (self):

        instances = [ i() for i in self.ITEMS ]
        list.__init__ (instances)