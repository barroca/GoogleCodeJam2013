def sqrt(x, eps=1e-9):
	r = x * 1.
	while abs(x - r * r) > eps:
		r = 0.5 * (r + x / r)
		return r

if __name__ == "__main__":
    print long(sqrt(256))

