
def num(x, y):
	i = 0
	numbers = []

	while i < int(x):
		print "At the top i is %d" % i
		numbers.append(i)
	
		i += int(y)
		print "Numbers now: ", numbers
		print "At the bottom i is %d" % i

	print "The numbers: "

	for num in numbers:
		print num
num(raw_input(),raw_input())
