
from sys import argv

script,filename = argv

print "We're going to erase%r." % filename
print "If you don't want that, hit CTRL-C (^c)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
target = open(filename)

print "file content is:"
print target.read()
target.close

target = open(filename, 'w')
print "Truncating the file. Goodbye!" 
#target.truncate()
target.close

target = open(filename, 'r+w')
print "file content is:"
print target.read()

print "Now I'm going to ask you for three lines."

l1 = raw_input("l1: ")
l2 = raw_input("l2: ")
l3 = raw_input("l3: ")

print "I'm goging to write these to the file."

target.write("%s\n%s\n%s\n" % (l1,l2,l3))
'''target.write("\n")
target.write(l2)
target.write("\n")
target.write(l3)
target.write("\n")'''
target.close
#after write should close then you can read.
target = open(filename)
print "file content is:"
print target.read()

print "And finally, we close it."
target.close()

