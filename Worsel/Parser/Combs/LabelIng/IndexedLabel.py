from Kit.Parts.Label        import Label
from Kit.Parts.Complaint    import Complaint
from Kit.Parts.DigitsParser import DigitsParser



class IndexedLabel (Label):
    'indexed statement label'

    SEQUENCE = DigitsParser

    def is_front_check (self, peek, check):

        status = check (peek)
        return (status == Complaint.SUCCESS)