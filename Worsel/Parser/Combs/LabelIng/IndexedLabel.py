from Kit.Parts.Label        import Label
from Kit.Parts.Complaint    import Complaint
from Kit.Parts.DigitsParser import DigitsParser



class IndexedLabel     (Label):
    'indexed statement label'

    SEQUENCE = DigitsParser


    def is_start       (self, peek, check):
        'logic to allow start of parse.'

        status = check (peek)
        return (status == Complaint.SUCCESS)
    

    def is_sense       (self, peek, check):
        'logic to allow contining of parse.'

        status = check (peek)
        return (status == Complaint.SUCCESS)