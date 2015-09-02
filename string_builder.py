class StringBuilder(object):
    def __init__(self):
        self.string = ''

    def append(self, value):
        self.string += str(value)
