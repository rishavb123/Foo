import sys

# filename = sys.argv[1]

filename = 'helloworld.foo'

f = open(filename, 'r')
f2 = open(filename.replace('.foo','-compressed.foo'),'w')
f2.write(f.read().replace("\n",""))
f.close()
f2.close()