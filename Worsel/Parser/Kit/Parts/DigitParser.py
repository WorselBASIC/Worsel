from Kit.Parts.Sequence  import Sequence
from Kit.Parts.Complaint import Complaint



class DigitParser:
    'parse a digit'

    DIGITS  = [ '0', '1', '2', '3',
                '4', '5', '6', '7', 
                '8', '9'
              ]
    
    RESULTS = [ Complaint.MATCH,
                Complaint.SUCCESS,
              ]


    def __init__ (self):
        pass


    def __call__ (self, data):
        return self.RESULTS [data in self.DIGITS]

