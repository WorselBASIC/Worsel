"""
" Test harness
"""
from sys         import argv
main   = argv [0]  # Where this file is
script = argv [1]  # BASIC script under test

from os.path import split 
from os.path import join 

app    = split (main)
test   = join  (app [0], script)

from Worsel.Lens.Lens import Lens
lens = Lens ()
lens ()