
import math


def nop():
	pass
def max(a,b):
	if (a>b):
		return a
	else:
		return b
		
#a = (int)(raw_input('Get max vaule of (a,b)\n'))
#b = (int)(raw_input())

a=3
b=33

print max(a,b)

def move(x,y,step,angle=0):
	_x = x + step * math.cos(angle)
	_y = y + step * math.sin(angle)
	return _x, _y

x, y = move(3.3,-3.0,7,math.pi/6)
print x, y

print [x*x for x in range(1,11) if x % 2 == 0]

print [m+n for m in 'ABC' for n in 'XYZ']

def fib(max):
	n,a,b = 0,0,1
	while n<max:
		yield b
		a,b = b,a+b
		n = n + 1
print fib(6)

for n in fib(6):
	print n

def add(x,y,f):
	return f(x) + f(y)
print add(-5,6,abs)

def is_prime(x):
	for i in range(2,(int)(math.sqrt(x))+1):
		if x%i==0:
			return False
	return True
print filter(is_prime,range(2,100))

class Student(object):
	
	def __init__(self, name, score):
		self.__name = name
		self.__score = score
	def print_score(self):
		print '%s: %s' % (self.__name,self.__score)

bart = Student('Bill', 90)

bart.print_score()

class Animal(object):
	pass
class Dog(Animal):
	pass
