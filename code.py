
def naive(a, b):
	x = a
	y = b
	z = 0

	while x > 0:
		x -= 1
		z += y
		print(z)
	return z

def russian(a,b):
	x = a	# Decrimenting x until 0
	y = b	# 
	z = 0
	while x > 0:
		if x % 2 == 1: # If x isn't even add y
			z += y
		y = y << 1 	   # Mulitply y by 2
		x = x >> 1 	   # Divide x by 2
	return z

def rec_russian(a, b):
	if a == 0: 	   # we are at the end of the line
		return 0
	if a % 2 == 0: # a is even divide by 2
		return 2 * rec_russian( a/2, b)
	return b + 2 * rec_russian((a-1)/2, b)
	