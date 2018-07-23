class InvalidCharacterException(Exception):
    def __init__(self, s, loc):
        super().__init__("foo files cannot contain any non foo characters such as '"+s+"' at line "+str(loc[0])+" character "+str(loc[1]))

class FooException(Exception):
    def __init__(self, c1, c2, c3):
        super().__init__(c1+c2+c3+" does not make a form of foo")