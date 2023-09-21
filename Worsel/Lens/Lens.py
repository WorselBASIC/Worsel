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
from Worsel.Parser.Block              import Block
from Worsel.Parser.Block              import hoist
from Worsel.Parser.StatementsComb     import StatementsComb
from Worsel.Parser.Kit.Tape.StdinTape import StdinTape
from Worsel.Parser.Kit.Tape.Tape      import setup

hoist (StatementsComb)  # recusion hoist
setup (StdinTape)       # default setting of BASIC input tape



class Lens (Block):
    'top-level execution point of BASIC parser'



""" End of Lens.py """