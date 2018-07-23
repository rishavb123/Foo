import sys
from fooexceptions import *
from util import to_foo_string

# filename = sys.argv[1]

f = open('helloworld-compressed.foo', 'r')
foocode = to_foo_string(f.read())
f.close()

for s in foocode:
    if s != ' ' and s != 'f' and s != 'F' and s != 'o' and s != 'O' and s != '[' and s != ']' and s != '(' and s != ')' and s != '{' and s != '}' and s != '\n' and s != '\t':
        raise InvalidCharacterException(s, foocode.locationof(s))

for i in range(len(foocode)-2):
    if foocode[i] == 'f' and (foocode[i+1] == 'f' or (foocode[i+2] == 'f' and foocode[i+1] == 'o')):
        raise FooException(foocode[i], foocode[i+1], foocode[i+2])

if "ooo" in foocode:
    raise FooException('o','o','o')

pythoncode = ""
temp=foocode.replace("\n",'')
goagain = True

specialcharacters = ['F','O','(',')','{','}','[',']',' ','\t']

while goagain:
    goagain = False
    for i in range(len(temp)):
        try:
            k = i*10 + specialcharacters.index(temp[i])
            pythoncode += chr(k)
            temp = temp[i+1:]
            goagain = True
            break
        except ValueError:
            pass
eval(pythoncode)