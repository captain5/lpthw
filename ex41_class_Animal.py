class Animal(object):
	pass

## ??
class Dog(Animal):
	
	def __init__(self, name):
		## ??
		self.name = name

## ??
class Cat(Animal):
	
	def __init__(self, name):
		self.name = name

## ??
class Person(object):
	
	def __init__(self, name):
		## ??
		self.name = name

		## Person has-a pet of some kind
		self.pet = None

## ??
class Employee(Person):
	
	def __init__(self, name, salary):
		## ?? hmm what is this strange magic?
		super(Employee, self).__init__(name)
		## ??
		self.salary = salary

## ??
class Fish(object):
	pass

## ??
class Salmon(Fish):
	pass

## ??
class Halibut(Fish):
	pass

## rover is-a Dog
rover = Dog("Rover")
print rover.name

## ?? 
satan = Cat("Satan")
print "Satan name is:", satan.name

## ??
mary = Person("Mary")
print "Mary name is:", mary.name

jack = Employee("jack", 20000)
print "jack name is:", jack.name,"and jack salary is:", jack.salary

