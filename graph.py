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

    def find_path(self, start_vertex, end_vertex, path=None):
        if path is None:
            path=[]
        graph = self.graph_dict
        path.append(start_vertex)
        if start_vertex == end_vertex:
            return path
        if start_vertex not in graph:
            return None
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_path = self.find_path(vertex, end_vertex, path)
                if extended_path:
                    return extended_path
        return None

    def find_path1(self, start, end, path):
        if path is None:
            path = []
        graph = self.graph_dict
        path.append(start)
        if start not in graph:
            return None
        if start == end:
            return path
        for vertex in graph[start]:
            if vertex not in path:
                extended_path = self.find_path1(vertex, end, extended_path)
                if extended_path:
                    return extended_path
        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]
        if start_vertex not in graph:
            return []
        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex,
                                                     end_vertex,
                                                     path)
                for p in extended_paths:
                    paths.append(p)
        return paths

if __name__ == "__main__":
    graph = {
        'a': ['c', 'f'],
        'b': ['c', 'e'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['c'],
        'f': ['d'],
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
    print("Path between a and d")
    path = graph.find_path("a", "f")
    print(path)
    print('All paths from vertex "c" to vertex "c":')
    path = graph.find_all_paths("a", "f")
    print(path)
    