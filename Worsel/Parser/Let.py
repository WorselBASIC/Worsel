from Kit.Parts.Token import Token
from Statement       import Statement 
from Expression      import Expression
from Tokens          import EndOfLineToken



class LetToken    (Token):
    MARKER = 'LET'


class AssignToken (Token)
    MARKER = '='



class LValue:
    pass


class LetStatement (Statement):

    @property
    def sequence (self):
        return [ LetToken,
                 LValue,
                 AssignToken,
                 Expression,
                 EndOfLineToken,
               ]