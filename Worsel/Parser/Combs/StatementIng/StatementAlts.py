from Kit.Parts.Sequence             import Sequence
from Parser.Combs.IfIng.If          import If
from Parser.Scans.LetScan.Let       import Let
from Parser.Scans.OptionScan.Option import Option
from Parser.Scans.EndScan.End       import End
from Parser.Scans.StopScan.Stop     import Stop
from Parser.Scans.RemScan.Rem       import Rem
from Parser.Scans.GotoScan.Goto     import Goto
from Parser.Scans.OnGotoScan.OnGoto import OnGoto



class StatementAlts (Sequence):
    'alternative choices for IF statement'

    ITEMS = [ Let,
              Option,
              Stop,
              End,
              Rem,
              Goto,
              OnGoto,
              If,
            ]