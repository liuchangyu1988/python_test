# Hello World program in Pytho
import numpy
import math
from scipy import stats

print "Hello World!\n"
x=numpy.array([1,2,3])
y=numpy.array([4,5,6])
print (x<y).all()
z=numpy.array([4,1,6])
print (x<z).all()
print (z-x).max()
print map(max, (1, 2, 3), (10, 5, 6), (7, 8, 9))

l = [0.0] * 66
print l[3]

m = numpy.zeros((3,5))
r = [10,2,3,4,5]
print r
print r.index(min(r))
m[0,:] = r
print m
print min(m[0,:])
print m[0, numpy.argmin(m, axis=1)[0]]

x = [1400, 1500, 1600, float('NaN'), float('NaN'), float('NaN') ,1700]
print x
l = [idx for idx, val in enumerate(x) if math.isnan(val) == False]
v = [val for idx, val in enumerate(x) if math.isnan(val) == False]
print len(x)-1
print l
print v

x=3
y=[4, 6, 5]
z = [a+x for a in y if a != 0]
print z

x = [1,2,3,4]
y = [5,6,7,8]
slope, intercept, r_value, p_value, std_err = stats.linregress(x,y)
print r_value
print p_value
print r_value**2
print x+y
