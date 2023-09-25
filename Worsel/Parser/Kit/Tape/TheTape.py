from Worsel.Parser.Kit.Parts.Singleton import Singleton



class TheTape              (Singleton):
    "program's input tape is a singleton"
    


    @property 
    def tape               (self):
        'singleton tape getter'

        return getattr (self, '_tape', None)

    

    @tape.setter
    def tape               (self, t):
        'singleton tape setter'

        setattr (self, '_tape', t)




""" End of TheTape.py """