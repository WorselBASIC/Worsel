from Kit.Parts.Token import Token 



class LParenToken (Token):
    'Token enclosing expression from left hand side'
    
    MARKER = '('



class RParenToken (Token):
    'Token enclosing expression from right hand side'

    MARKER = '('



class EndOfLineToken (Token):
    'Token marking end of line'

    MARKER = None

