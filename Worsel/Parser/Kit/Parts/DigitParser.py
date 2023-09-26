from Kit.Parts.Sequence  import Sequence
from Kit.Parts.Complaint import Complaint



class DigitParser:
    'parse each digit'

    LIMIT  = 32
    DIGITS = [ '0', '1', '2', '3',
               '4', '5', '6', '7', 
               '8', '9'
             ]


    def __init__   (self):

        self.result = []
        self.length = 0


    def __call__   (self, data):

        if (self.length > self.LIMIT):
            return Complaint.LIMIT 
        
        if (data not in self.DIGITS):
            return Complaint.MATCH 
        
        return Complaint.SUCCESS
