class Complaint:
    'complaints to user'

    SUCCESS      = 0
    ACCEPT       = 1
    LIMIT        = 2
    MATCH        = 3
    PRECONDITION = 4

    def __call__ (self, *argv):
        'complain to user'