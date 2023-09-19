"""
" File:      Statements.py
" Purpose:   Current set of statements in language  
" 
" Copyright: (c) 2023 by Worsel BASIC Working Group 
"            All Rights Reserved.
"
" License:   Creative Commons
"            Share-Alike With Attribution Required 
"            License Version 3.0
"            Commercial Use Allowed With Above Terms
"""



"""
" This file uses the following libraries:
"""
from DataStatement       import DataStatement
from DefinitionStatement import DefinitionStatement
from DimensionStatement  import DimensionStatement
from GosubStatement      import GosubStatement
from GotoStatement       import GotoStatement 
from IfThenStatement     import IfThenStatement
from LetStatement        import LetStatement 
from OnGotoStatement     import OnGotoStatement 
from OptionStatement     import OptionStatement 
from PrintStatement      import PrintStatement 
from RandomizeStatement  import RandomizeStatement
from ReadStatement       import ReadStatement 
from RemarkStatement     import RemarkStatement 
from ReturnStatement     import ReturnStatement 
from StopStatement       import StopStatement 



CMDL_Statements = [
    DataStatement,
    PrintStatement,
    RandomizeStatement,
    ReadStatement,
]



EMBD_Statements = [
    DefinitionStatement,
    DimensionStatement, 
    GosubStatement, 
    GotoStatement,
    IfThenStatement,
    LetStatement, 
    OnGotoStatement,   
    OptionStatement, 
    RemarkStatement,
    ReturnStatement,
    StopStatement,
]



class Statements (set):
    'current set of statements in language'

    def __init__ (self):
        set.__init__ (self, EMBD_Statements)



""" End of Statements.py """