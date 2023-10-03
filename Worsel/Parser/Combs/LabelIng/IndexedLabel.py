from Kit.Parts.Label        import Label
from Kit.Parts.Complaint    import Complaint
from Kit.Parts.DigitsParser import DigitsParser



class IndexedLabel     (Label):
    'indexed statement label'

    SEQUENCE = DigitsParser
    LIMIT    = 32


    def __init__       (self):

        Label.__init__ (self)
        self.result = ''


    def is_start       (self, peek, check):
        'logic to allow start of parse.'

        status = check (peek)
        return (status == Complaint.SUCCESS)
    

    def is_sense       (self, peek, check):
        'logic to allow contining of parse.'

        if (len (self.result) >= self.LIMIT):
            return Complaint.LIMIT

        status = check (peek)

        if (status != Complaint.SUCCESS):
            return status
    
        self.advance ()
        
        return Complaint.SUCCESS
