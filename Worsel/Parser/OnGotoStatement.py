from Statement import Statement 



class OnGotoStatement (Statement):

    @property
    def sequence (self):
        return [ 'ON',
                 Expression,
                 'GOTO'
                 Expression,
                 EndOfLine
               ]