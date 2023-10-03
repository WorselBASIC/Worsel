"""
" This file uses the following libraries:
"""
from Worsel.Parser.Kit.Stack.TheStack import TheStack
from Worsel.Parser.Kit.Tape.TheTape   import TheTape
from Sequence                         import Sequence
from Complaint                        import Complaint



class Filter:
    'contains parsing primitives'

    PRECONDITION = None
    SEQUENCE     = Sequence


    def __init__        (self):

        self.precondition = None 

        if (self.PRECONDITION != None):
            self.precondition  = self.PRECONDITION ()

        self.is_in_use    = False
        self.complaint    = Complaint ()
        self._sequence    = self.SEQUENCE ()


    @property 
    def sequence        (self):
        'the sequence of items being filtered'

        return self._sequence
    

    @property 
    def start           (self):
        """
        criteron for start of parse.
        override as needed.
        """

        if (len (self.sequence) == 0):
            return None
        
        begin = self.sequence [0]
        return begin
    

    @property 
    def sense           (self):
        """
        criteron for next in parse.
        override as needed.
        """

        if (len (self.sequence) == 0):
            return None
        
        begin = self.sequence [0]
        return begin


    def is_start        (self, peek, check):
        """
        logic to allow start of parse.
        override as needed.
        """

        return False 
    

    def is_sense        (self, peek, check):
        """
        logic to allow continuing parse.
        override as needed.
        """

        return False 
    

    def advance         (self):
        'advance to next symbol in tape'

        TheTape().tape.advance ()


    @property 
    def next            (self):
        'short cut to next in tape'

        result = TheTape().tape.peek
        return result


    @property 
    def is_acceptable   (self):
        'begin parse at start of sequence?'

        return self.is_start (self.next, self.start)


    @property 
    def is_parseable    (self):
        'continue parse?'

        return self.is_sense (self.next, self.sense)


    @property 
    def me              (self):
        'shortcut for read stack'

        return TheStack ().stack.front
    

    @me.setter 
    def me              (self, value):
        'shortcut for push stack'

        TheStack ().stack.front = value


    def __call__        (self):
        'parse next datum'

        # advances current statement
        if self.is_in_use:  
            return self.me.is_parseable

        # if this statement is not yet advanced,
        # push possible precondition onto the stack
        if self.precondition:
            self.me = self.precondition 
            return Complaint.PRECONDITION

        return Complaint.SUCCESS
        