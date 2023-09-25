"""
" This file uses these libraries:
"""
from Kit.Parts.Block import Block as _Block



class Block (_Block):
    'take block of BASIC statements'

    COMB = None

    def __init__ (self):
        _Block.__init__ (self)



def hoist   (klass):
    """
    Modify Block dynamically to avoid
    Python recursive reference error.
    """
    Block.COMB = klass
    x = Block.COMB  # debugging test point



""" End of Block.py """