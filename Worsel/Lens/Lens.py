"""
" Dynamic relative path import hook
"""
import sys
import os

x0 = __file__
x1 = os.path.split (x0)
x2 = os.path.split (x1 [0])
x3 = x2 [0]         # Determine project root

x4a = os.path.join  (x3, 'Parser')
x4b = os.path.join  (x3, 'Parser/Kit/Parts')
x4c = os.path.join  (x3, 'Parser/Kit/Stack')
x4d = os.path.join  (x3, 'Parser/Kit/Tape')

sys.path.append (x3)
sys.path.append (x4a)
sys.path.append (x4b)
sys.path.append (x4c)
sys.path.append (x4d)



"""
" This file uses the following libraries
"""
from Worsel.Parser.ParserBlock                       import ParserBlock
from Worsel.Parser.ParserBlock                       import hoist
from Worsel.Parser.Combs.StatementIng.StatementsComb import StatementsComb

hoist (StatementsComb)  # recusion hoist



class Lens (ParserBlock):
    'top-level execution point of BASIC parser'

    def __init__ (self):
        ParserBlock.__init__ (self)



""" End of Lens.py """