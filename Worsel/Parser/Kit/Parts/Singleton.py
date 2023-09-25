"""
Per https://stackoverflow.com/questions/12305142/issue-with-singleton-python-call-two-times-init
"""


class Singleton (object):
    'creates singleton out of any klass'

    def __new__ (klass, *args, **kwargs):

        try:
            return klass._instance
        
        except AttributeError:
            val = klass._instance = object.__new__ (klass, *args, **kwargs)
            return val