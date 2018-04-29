import jobimcount
import pmi

class Vertex:
    def __init__(self, node):
        self.id = node
        self.adjacent = {}

    def __str__(self):
        return str(self.id) + ' adjacent: ' + str([x.id for x in self.adjacent])

    def add_neighbor(self, neighbor, weight=0):
        self.adjacent[neighbor] = weight

    def get_connections(self):
        return self.adjacent.keys()  

    def get_id(self):
        return self.id

    def get_weight(self, neighbor):
        return self.adjacent[neighbor]

class Graph:
    def __init__(self):
        self.vert_dict = {}
        self.num_vertices = 0

    def __iter__(self):
        return iter(self.vert_dict.values())

    def add_vertex(self, node):
        if node in self.vert_dict:
            return Vertex(node)
        self.num_vertices = self.num_vertices + 1
        new_vertex = Vertex(node)
        self.vert_dict[node] = new_vertex
        return new_vertex

    def get_vertex(self, n):
        if n in self.vert_dict:
            return self.vert_dict[n]
        else:
            return None

    def add_edge(self, frm, to, cost = 0):
        if frm not in self.vert_dict:
            self.add_vertex(frm)
        if to not in self.vert_dict:
            self.add_vertex(to)

        self.vert_dict[frm].add_neighbor(self.vert_dict[to], cost)
        self.vert_dict[to].add_neighbor(self.vert_dict[frm], cost)

    def get_vertices(self):
        return self.vert_dict.keys()



graph = Graph()

for jo_bim, sigval in pmi.sig_score.items():
    jo = jo_bim.split('\t')[0]
    bim = jo_bim.split('\t')[1].split('\n')[0]
    graph.add_vertex(jo)
    graph.add_vertex(bim)

    graph.add_edge(jo,bim,sigval)
    graph.add_edge(bim,jo,sigval)

# aggregate = {}

# for bim in jobimcount.Bim_dict:
#     similar_to = []
#     if bim in graph.vert_dict:
#         jos_neighbor = graph.vert_dict[bim].get_connections()
#         for neighbor in jos_neighbor:
#             # print(neighbors.get_id())
#             similar_to.append(neighbor.get_id())
#     if(len(similar_to) >= 4):
#         aggregate[bim] = similar_to

jos_agg = {}
jos_spliced = {}


for jo1 in jobimcount.Jo_dict:
    jos_agg[jo1] = {}
    if jo1 in graph.vert_dict:
        bim_neighbors = graph.vert_dict[jo1].get_connections()
        for bim_ver in bim_neighbors:
            bim = bim_ver.get_id()
            jo2_neighbors = graph.vert_dict[bim].get_connections()
            for jo2_ver in jo2_neighbors:
                jo2 = jo2_ver.get_id()
                if jo2 in jos_agg[jo1]:
                    jos_agg[jo1][jo2] += 1
                else:
                    jos_agg[jo1][jo2] = 1

for jo in jos_agg:
	jos_spliced[jo.split('#')[0]] = jos_agg[jo]
# print(jos_agg)