class Sample(object):
    def three_fields(self):
        self.third_field = 0
        self.b = self.third_field
        if self.a == self.b:
            self.a = self.third_field
