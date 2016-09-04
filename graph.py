class Graph:
    def __init__(self, graph_dict=None):
        if graph_dict is None:
            graph_dict = {}
        self.graph_dict = graph_dict

    def add_vertex(self, vertex):
        if vertex not in self.graph_dict:
            self.graph_dict[vertex] = []

    def add_edge(self, edge):
        edge = set(edge)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.graph_dict:
            if vertex2 not in self.graph_dict[vertex1]:
                self.graph_dict[vertex1].append(vertex2)
            else:
                print("Vertices already connected")
        else:
            self.add_vertex(vertex1)
            if vertex2 not in self.graph_dict:
                self.add_vertex(vertex2)
            self.graph_dict[vertex1].append(vertex2)

    def get_vertices(self):
        return sorted(self.graph_dict.keys())

    def get_edges(self):
        list = []
        for node in self.graph_dict:
            for neighbour in self.graph_dict[node]:
                list.append((node, neighbour))
        return list

    def get_isolated_vertices(self):
        list = []
        for node in self.graph_dict:
            if not self.graph_dict[node]:
                list += node
        return list

    def __str__(self):
        res = "vertices:"
        for x in self.graph_dict:
            res += str(x) + " "
        res += "\n Edges:"
        for edge in self.get_edges():
            res += str(edge)
        return res


if __name__ == "__main__":
    graph = {
        'a': ['c'],
        'b': ['c', 'e'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['c'],
        'f': []
    }
    graph = Graph(graph)

    print("VERTICES:")
    print(graph.get_vertices())
    print("EGDES:")
    print(graph.get_edges())
    print("ISOLATED VERTICES:")
    print(graph.get_isolated_vertices())
    print("Adding an edge {'x','y'}")
    graph.add_edge(('x','y'))
    print(graph.get_vertices())
    print(graph.get_edges())
