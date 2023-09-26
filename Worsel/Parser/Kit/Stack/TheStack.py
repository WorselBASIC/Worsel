from Worsel.Parser.Kit.Parts.Singleton import Singleton



class TheStack             (Singleton):
    "program's parse stack is a singleton"
    

    @property 
    def stack              (self):
        'singleton stack getter'

        return getattr (self, '_stack', None)

    

    @stack.setter
    def stack              (self, s):
        'singleton stack setter'

        setattr (self, '_stack', s)




""" End of TheStack.py """