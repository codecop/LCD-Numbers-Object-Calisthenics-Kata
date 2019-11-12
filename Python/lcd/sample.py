class Sample(object):
    def __init__(self):
        self._a = 0
        self._b = 0
        self._third_field = 0  # ! third field

    def with_else(self):
        if self._a == self._b:
            self._a = self._third_field
        else:  # ! else
            self._b = self._third_field
