from sys import argv
from os.path import exists
'''
script,from_file,to_file = argv

print "Copying form %s to %s" % (from_file, to_file)

#you can also use like this:
#in_file = open(from_file).read()
in_file = open(from_file)
indata = in_file.read()

print "The input file is %d bytes long" % len(indata)

print "Does the output file exist? %r" % exists(to_file)
print "Ready, hit RETURN to continue, CTRL-C to abort."
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)

print "Alright, all done."

out_file.close()
in_file.close() 
'''
open(argv[2], 'w').write(open(argv[1]).read())
