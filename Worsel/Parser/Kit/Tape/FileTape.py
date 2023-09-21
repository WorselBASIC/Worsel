from .Tape import Tape as _Tape


class FileTape (_Tape):
    'tape from file'


    def __init__ (self, filename):
        _Tape.__init__ (self)

        self.file   = open (filename)
        self._width = 1


    @property
    def next     (self):
        x = self.file.read ()
        return x