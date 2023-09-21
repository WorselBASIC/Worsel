"""
" This file uses these libraries:
"""
from Kit.Parts.Block import Block as _Block



class Block (_Block):
    'take block of BASIC statements'

    COMB = None



def hoist   (klass):
    """
    Modify Block dynamically to avoid
    Python recursive reference error.
    """
    Block.COMB = klass



""" End of Block.py """