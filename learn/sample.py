
# -*- coding: utf-8 -*-

print "hello world ," , "Are you ok"
print "100 + 200 = " , 100+200

name = raw_input('what\'s your name?\n')
print "hello," , name

# print abs(a)
a = (int)(raw_input('Get abs of an integer\n'))

if a > 0:
	print a
else:
	print -a

print '''line1
line2
line3'''

print u'中文'

print 'Today is %d-%02d-%d' % (2017,7,14)
print '%d %% %d = %d' % (10,3,1)

#list
p = ['a', 'b']
s = ['c', 'd', p, 'e']
print s[2][1]

#tuple
t = (1,2,3)
print t

age = 20
if age>=6:
	print 'teenager'
elif age>=18:
	print 'adult'
else:
	print 'kid'

names = ['Michael', 'Bob', 'Lily']
for name in names:
	print name

for x in [3,33,333,3333,33333]:
	print x
	
for x in range(5):
	print x

#dict	(map)
d = {'Michael': 95, 'Bob': 93, 'Lily':85}
print "Bob:", d['Bob']
d['Alice']=60
print "Alice:", d['Alice']
d.pop('Michael')
print d


s = set([1,1,3,3,3,3,2])
print s
s2 = set([2,5])
print s&s2
print s|s2