class Graph:
    vertices = {}
    time = 0

    def __init__(self, vertices={}):
        self.vertices = vertices

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        vertices = self.vertices
        if u in vertices and v in vertices:
            for key, value in vertices.items():
                if key == u:
                        value.add_neighbour(v)
                if key == v:
                        value.add_neighbour(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in set(arr(self.vertices.keys())):
            print(key + str(self.vertices[key].neighbours) + "  " + str(self.vertices[key].discovery) + "/" + str(self.vertices[key].finish))

    def _dfs(self, vertex):
        global time
        vertex.discovery = time
        vertex.color = 'red'
        time += 1
        for v in vertex.neighbours:
            if self.vertices[v].color == 'black':
                self._dfs(self.vertices[v])
        vertex.color = 'blue'
        vertex.finish = time
        time += 1

    def dfs(self, vertex):
        global time
        time = 1
        self._dfs1(vertex)

    def _dfs1(self,vertex):
        global time
        vertex.color = 'red'
        vertex.discovery = time
        for v in vertex.neighbours:
            if self.vertices[v].color == 'black':
                self._dfs1(self.vertices[v])
        vertex.color = 'blue'
        vertex.finish = time
        time += 1


class Vertex:
    def __init__(self, name):
        self.name = name
        self.neighbours = arr()

        self.discovery = 0
        self.finish = 0
        self.color = 'black'

    def add_neighbour(self, v):
        nset = set(self.neighbours)
        if v not in nset:
            self.neighbours.append(v)
            self.neighbours.sort()

'''
if __name__ != "__main__":
    graph = Graph()
    for i in range(ord('A'), ord('H')):
        graph.add_vertex(Vertex(chr(i)))
edges = ['AB', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    graph.add_edge(edge[:1], edge[1:])
graph.dfs(graph.vertices['A'])
graph.print_graph()'''

if __name__ == "__main__":
    arr = []
    for i in range(0,5):
        temp = list()
        for j in range(0, 5):
            temp.append(j)
        arr.append(temp)
    print(arr)
    print(arr[1][4])
