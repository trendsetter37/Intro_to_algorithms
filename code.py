
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

def find_eulerian_tour(graph): # Doesn't work right when submitted
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

from collections import defaultdict
from random import choice
def find_eulerian_tour2(graph):
	''' Credit: http://forums.udacity.com/questions/100157003/discussion-of-possible-solution-algorithms-ps1-10#cs215#answer-container-100157510 '''
    # nodes: dictionary of edges to travel in the form {node: list of nodes connected to that node}
    nodes = defaultdict(list)
    for k,l in graph:
        nodes[k].append(l)
        nodes[l].append(k)

    # pick a random node to begin the path
    node = choice(nodes.keys())
    path = [node]

    # traverse the graph. remove used edges as you go
    while len(nodes[node]) > 0 :
        after = nodes[node].pop()
        nodes[after].remove(node)      
        path.append(after)
        node = after

    # find nodes in our path that still have unused edges
    for node, node_list in nodes.iteritems():
        if node in path and len(node_list)>0:

            # insert "detour" into our path. as before, remove edges as you go
            index = path.index(node)
            while len(nodes[node]) > 0 :
                after = nodes[node].pop()
                nodes[after].remove(node)
                index+=1
                path.insert(index,after)
                node = after

    return path	