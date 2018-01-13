class FieldsSample(object):
    def three_fields(self):
        self.third_field = 0
        self.b = self.third_field
        if self.a == self.b:
            self.a = self.third_field


class IndentationSample(object):
    def one_level_of_indent(self):
        self.a = 1
        if self.a > 1:
            self.a = 1

    def two_levels_of_indent(self):
        self.a = 1
        if self.a > 1:
            if self.a > 2:
                self.a = 1


class ElseSample(object):
    def uses_else(self):
        self.a = 1
        if self.a > 1:
            self.a = 1
        else:
            self.a = 2
