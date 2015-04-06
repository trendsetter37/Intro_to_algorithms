
def naive(a, b):
	x = a
	y = b
	z = 0

	while x > 0:
		x += y
		z -= 1
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

	