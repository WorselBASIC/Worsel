from Kit.Parts.Filter import Filter
from Stack            import Stack



class Comb (Filter):
    'Filter input for a language construction'

    PRECONDITION  = None
    ALTERNATIVES  = None


    def __init__        (self):

        self.precondition = None 

        if (self.PRECONDITION != None):
            self.precondition  = self.PRECONDITION () 

        self.alternatives = None 

        if (self.ALTERNATIVES != None):
            self.alternatives  = self.ALTERNATIVES ()

        Filter.__init__ (self)
        

    def __call__        (self):
        'parse next datum in current statement'

        use_this_alternative = None 

        # advances current statement
        if self.is_in_use:
            return Stack.rear (None)

        # no current statement yet?
        if self.precondition:
            if (status := self.precondition ()):
                return self.complain (status, self, tape)
        
        # find the statement beginning match
        for alternative in self.alternatives:
            if (alternative.is_acceptable):
                use_this_alternative = alternative
                
        # no statement matches?
        if (not use_this_alternative):
            return self.complaint (self.complaint.ACCEPT,
                                   self,
                                   tape)

        # set up current statement on top of stack.
        # (we use a stack because we want a 
        #  non-recursive parser design which we
        #  can more easily port away from Python)       
        Stack.put (use_this_alternative(), tape)
        self.is_in_use    = True
        Stack.rear.index += 1 

            

            
  
                              
