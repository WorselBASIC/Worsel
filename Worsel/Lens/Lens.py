"""
" Dynamic relative path import hook
"""
import sys
import os

x0 = __file__
x1 = os.path.split (x0)
x2 = os.path.split (x1 [0])
x3 = x2 [0]
x4 = os.path.join  (x3, 'Parser')

sys.path.append (x3)
sys.path.append (x4)



"""
" This file uses the following libraries
"""
from Worsel.Parser.Block import StatementBlock



class Lens (StatementBlock):
    pass



"""
" Test harness
"""
if __name__ == '__main__':
    lens = Lens ()
    lens ()