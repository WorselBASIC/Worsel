"""
" This file uses these libraries:
"""
from Kit.Parts.Block import Block



class ParserBlock (Block):
    'take block of BASIC statements'

    COMB = None

    def __init__ (self):
        Block.__init__ (self)



def hoist   (klass):
    """
    Modify Block dynamically to avoid
    Python recursive reference error.
    """
    ParserBlock.COMB = klass
    x                = ParserBlock.COMB  # debugging test point



""" End of Block.py """