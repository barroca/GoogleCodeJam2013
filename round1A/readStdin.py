def pr(a,b):
	print a
	print "---"
	print b
	return 0

for testcase in xrange(input()):
	a,b = map(int, raw_input().split())
	print "Case #%d: %d" % (1 + testcase, pr(a,b))
