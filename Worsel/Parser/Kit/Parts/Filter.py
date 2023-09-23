"""
" This file uses the following libraries:
"""
from Kit.Stack.Stack import Stack
from Complaint import Complaint



class Filter:
    'contains parsing primitives'

    def __init__        (self):
        self.index     = 0 
        self.is_in_use = False
        self.complaint = Complaint ()


    @property 
    def sequence        (self):
        'the sequence of items being filtered'

        return []


    def is_acceptable   (self, datum):
        'may we begin parse with this sequence?'

        return datum == (self.sequence [0])


    def __call__        (self, datum):
        Stack.put       (self, datum)
