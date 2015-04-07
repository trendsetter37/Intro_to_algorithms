
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

def find_eulerian_tour(graph):
	''' can be found at http://stackoverflow.com/questions/12447880/finding-a-eulerian-tour#answer-12458027 '''
	tour = [] # building up result here

	current_vertex = graph[0][0]
	tour.append(current_vertex)

	while len(graph) > 0:
		
		for edge in graph:
			if current_vertex in edge:
				if edge[0] == current_vertex:
					current_vertex = edge[1]
				else:
					current_vertex = edge[0]
				graph.remove(edge)
				tour.append(current_vertex)
				break
		else:
			# Edit to account for case no tour is possible
			return False
	return tour

	