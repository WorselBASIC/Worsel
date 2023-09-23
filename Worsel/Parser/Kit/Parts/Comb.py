from Kit.Parts.Filter import Filter
from Stack            import Stack



class Comb (Filter):
    'Filter input for a language construction'

    PRECONDITION  = None
    ALTERNATIVES  = []


    def __init__        (self):
        Filter.__init__ (self)
        self.precondition    = self.PRECONDITION
        self.alternatives    = self.ALTERNATIVES


    def __call__        (self, tape):
        'parse next datum in current statement'

        use_this_alternative = None 

        # advances current statement
        if self.is_in_use:
            return Stack.rear (tape)

        # no current statement yet?
        if self.precondition:
            if (status := self.precondition (self, tape)):
                return self.complain (status, self, tape)
        
        # find the statement beginning match
        for alternative in self.alternatives:
            if (self.alternative.is_acceptable (tape)):
                use_this_alternative = alternative
                
        # no statement matches?
        if (not use_this_alternative):
            return self.complain (self.COMPLAIN.ACCEPT,
                                  self,
                                  tape)

        # set up current statement on top of stack.
        # (we use a stack because we want a 
        #  non-recursive parser design which we
        #  can more easily port away from Python)       
        Stack.put (use_this_alternative(), tape)
        self.is_in_use    = True
        Stack.rear.index += 1 

            

            
  
                              
