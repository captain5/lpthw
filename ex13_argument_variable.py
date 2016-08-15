from sys import argv

script, first, second, third = argv

print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third

name = raw_input("Your name:")
age = raw_input("Your age:")
print "So,Your name is %s,your age is %s." % (name, age)
