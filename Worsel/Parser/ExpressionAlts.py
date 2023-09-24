from Kit.Parts.Sequence import Sequence
from Dyads              import AdditionDyad 
from Dyads              import SubtractionDyad 
from Dyads              import MultiplicationDyad 
from Dyads              import DivisionDyad 
from Dyads              import SequenceDyad 
from Dyads              import GEDyad 
from Dyads              import GTDyad 
from Dyads              import LTDyad 
from Dyads              import LEDyad 
from Dyads              import NEDyad
from Dyads              import EQDyad



class ExpressionAlts (Sequence):
    'alternative choices for expression'

    ITEMS = [ AdditionDyad,
              SubtractionDyad, 
              MultiplicationDyad,
              DivisionDyad,
              SequenceDyad,
              GEDyad,
              GTDyad,
              LEDyad,
              LTDyad,
              NEDyad,
              EQDyad,
            ]