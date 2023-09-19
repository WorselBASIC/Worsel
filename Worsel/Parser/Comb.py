from Filter      import Filter
from Stack.Stack import Stack



class Comb (Filter):
    'Filter input for a language construction'

    PRECONDITION  = None
    ALTERNATIVES  = []


    def __init__        (self):
        Filter.__init__ (self)
        self.precondition    = self.PRECONDITION
        self.alternatives    = self.ALTERNATIVES


    def __call__        (self, datum):
        'parse next datum in current statement'

        use_this_alternative = None 

        # advances current statement
        if self.is_in_use:
            return Stack.rear (datum)

        # no current statement yet?
        if self.precondition:
            if (status := self.precondition (self, datum)):
                return self.complain (status, self, datum)
        
        # find the statement beginning match
        for alternative in self.alternatives:
            if (self.alternative.is_acceptable (datum)):
                use_this_alternative = alternative
                
        # no statement matches?
        if (not use_this_alternative):
            return self.complain (self.COMPLAIN.ACCEPT,
                                  self,
                                  datum)

        # set up current statement on top of stack.
        # (we use a stack because we want a 
        #  non-recursive parser design which we
        #  can more easily port away from Python)       
        Stack.put (use_this_alternative(), datum)
        self.is_in_use    = True
        Stack.rear.index += 1 

            

            
  
                              
