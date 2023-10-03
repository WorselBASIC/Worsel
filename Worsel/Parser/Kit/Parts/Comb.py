from Kit.Parts.Filter                 import Filter
from Worsel.Parser.Kit.Stack.TheStack import TheStack
from Kit.Parts.Complaint              import Complaint



class Comb (Filter):
    'Filter input for a language construction'

    ALTERNATIVES  = None


    def __init__        (self):

        Filter.__init__ (self)
 
        self.alternatives = None 

        if (self.ALTERNATIVES != None):
            self.alternatives  = self.ALTERNATIVES ()


    @property
    def alternative     (self):
        for a in self.alternatives:
            if (a.is_acceptable):
                return a

        

    def __call__        (self):
        'parse next datum'
                                
        status = Filter.__call__ (self)

        if (status != Complaint.SUCCESS):
            if (status == Complaint.PRECONDITION):
                return Complaint.SUCCESS
            else:
                return status
        
        if (match  := self.alternative): 
            self.me           = match 
            self.me.is_in_use = True
            return Complaint.SUCCESS
    
        return Complaint.ACCEPT


            

            
  
                              
