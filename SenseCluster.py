import agg_graph
import jobimcount
from math import random

unclustered = Graph()
count = []

for jo, jo_sim in agg_graph.jos_agg.items():
	unclustered.add_vertex(jo)
	for jo2 in jo_sim:
		unclustered.add_vertex(jo2)
		unclustered.add_edge(jo, jo2, 1)
		count[jo] += 1
		count[jo2] += 1

i = 0

for vertex in unclustered:
	vertex.clust = i++


done = []

while True:
	maxcount = -1
	num = random.randint(0, i)
	maxvertex = unclustered.get_vertices(num)
	#randVert = unclustered.get_vertex(maxvertex)
	if num not in done:
		for w in unclustered:
			if Edge(v, w) and  count[w] > maxcount:
				maxcount = count[w]
				maxvertex = w
		num.clust = maxvertex.clust
		done.append(num)
	else if len(done) == len(unclustered.vert_dict):
		break