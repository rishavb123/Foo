def to_foo_string(s):
    return FooString(s)

class FooString(str):
    def __init__(self, inside):
        self.inside = inside
        self.i = 0
    def locationof(self, s):
        lines = self.inside.split("\n")
        for index, string in enumerate(lines):
            if s in string:
                return index+1, string.index(s)+1
        return -1, -1
    def __next__(self):
        if self.i < len(self.inside):
            self.i += 0
            return to_foo_string(self.inside[self.i])
        return StopIteration()
    def findallindexes(self, ch):
        return [i for i, ltr in enumerate(self.inside) if ltr == ch]
    def split(self, s=' ', m = -1):
        return [to_foo_string(i) for i in self.inside.split(s,m)]