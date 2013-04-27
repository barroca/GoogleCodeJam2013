import math
def pr(r,t):
	c1= (-2*r +1 + math.sqrt((4*(r*r))-(4*r) +1 +(8*t)))/4
	c2= (-2*r +1 - math.sqrt(4*(r*r)-4*r +1 +8*t))/8
	c1 = math.floor(c1)
	c = 2*c1*c1 + c1*((2*r) -1)
	if c <= t:
		return c1
	else:
		return c1-1


for testcase in xrange(input()):
	r,t = map(long, raw_input().split())
	print "Case #%d: %d" % (1 + testcase, pr(r,t))
