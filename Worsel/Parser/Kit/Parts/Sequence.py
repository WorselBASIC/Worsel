class Sequence (list):
    'overrideable list object, possibly empty'

    ITEMS = []

    def __init__      (self):
        list.__init__ (self, self.ITEMS)