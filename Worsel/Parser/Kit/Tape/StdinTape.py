from Tape import Tape as _Tape



class _GetchUnix:
    """
    unbuffered character read from unix
    https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
    """

    def __init__(self):
        import tty, sys

    def __call__(self):
        import sys, tty, termios
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(sys.stdin.fileno())
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch



class _GetchWindows:
    """
    unbuffered character read from windows
    https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
    """

    def __init__(self):
        import msvcrt

    def __call__(self):
        import msvcrt
        return msvcrt.getch()



class _Getch:
    """
    unbuffered character read
    https://stackoverflow.com/questions/510357/how-to-read-a-single-character-from-the-user
    """

    def __init__(self):
        try:
            self.impl = _GetchWindows()
        except ImportError:
            self.impl = _GetchUnix()

    def __call__(self): return self.impl()




class StdinTape  (_Tape):
    'tape from standard input'

    def __init__ (self):
        Tape.__init__ (self)
        self._width = 1

    @property
    def next     (self):
        return _Getch ()
