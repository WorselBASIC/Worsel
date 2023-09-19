from Statement import Statement 



class GotoStatement (Statement):

    @property
    def sequence (self):
        return [ 'GOTO'
                 Expression,
                 EndOfLine
               ]