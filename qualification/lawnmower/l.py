import sys


def validate(matrix,a,b,size):
	if matrix[a][b] == 1:
		sl = True
		sc = True
		for i in range(size[1]):
			if matrix[a][i] == 2:
				sl = False
				break
		for j in range(size[0]):
			if matrix[j][b] == 2:
				sc = False
				break
		if sl or sc:
			return False
		return True
	
my_file = open(sys.argv[1], 'r')


tests = int(my_file.readline())
for i in range(tests):
	matrix = []
	ll = map (int, my_file.readline().split(" "))
	message = "YES"
	if (ll[0] >1 and ll[1] >1):
		for a in range(ll[0]):
			tx = (my_file.readline()).rstrip('\n').split(" ")
			matrix.append(map(int,tx))
		ret = False
		for a in range(ll[0]):
			for b in range (ll[1]):
				if validate(matrix,a,b,ll):
					ret = True
					break
			if ret:
				message = "NO"
				break
	else:
		for s in range(ll[0]):
			my_file.readline()
	print "Case #{0}: {1}".format((i+1),message)


