class Graph:

    def __init__(self):
        self.vertex_count = 0
        self.vertex_list = list()
        self.adjMatrix = []

    def add_vertex(self, label):
        self.vertex_count += 1
        temp = []
        for i in range(0, self.vertex_count):
            temp.append(0)
        self.adjMatrix.append(temp)
        for i in range(0, self.vertex_count-1):
            self.adjMatrix[i].append(0)
        self.vertex_list.append(Vertex(label))

    def add_edge(self, u, v):
        if (u >= 0) and (u < self.vertex_count) and (v >= 0) and (v < self.vertex_count):
            self.adjMatrix[u][v] = 1
            self.adjMatrix[v][u] = 1
        else:
            print("Vertex does not exist. Add the vertex first.")

    def display_vertex(self, v_index):
        # Print the label attribute of the object at 'v_index' index in the vertex list.
        print(self.vertex_list[v_index].label)

    def display_graph(self):
        for vertex in self.vertex_list:
            print(vertex.label)

    def display_edges(self):
        print("Adjacency Matrix :")
        for i in range(0, self.vertex_count):
            print(chr(65+i), " : ", self.adjMatrix[i])

    def get_unvisited_vertex(self, v):
        for j in range(0, self.vertex_count):
            if self.adjMatrix[v][j] == 1 and self.vertex_list[j].visited is False:
                return j
        return -1

    def dfs(self):
        self.vertex_list[0].visited = True
        self.display_vertex(0)
        s = [0]
        top = 0
        while top != -1:
            v = self.get_unvisited_vertex(s[top])
            if v == -1:
                s.pop()
                top -= 1
            else:
                self.display_vertex(v)
                self.vertex_list[v].visited = True
                s.append(v)
                top += 1
        for i in range(0, self.vertex_count):
            self.vertex_list[i].visited = False

    def bfs(self, start):
        vertex_q = []
        self.vertex_list[start].visited = True
        cur = start
        v = self.get_unvisited_vertex(cur)
        vertex_q.append(v)
        self.vertex_list[v].visited = True
        flag = True
        while flag:

            self.display_vertex(cur)
            v = self.get_unvisited_vertex(cur)
            if v != -1:
                self.vertex_list[v].visited = True
                vertex_q.append(v)
            while v != -1:
                v = self.get_unvisited_vertex(cur)
                if v != -1:
                    self.vertex_list[v].visited = True
                    vertex_q.append(v)
            if len(vertex_q) == 0:
                break
            if v == -1:
                cur = vertex_q[0]
                vertex_q = vertex_q[1:]
        for i in range(0, self.vertex_count):
            self.vertex_list[i].visited = False


class Vertex:
    def __init__(self, label):
        self.label = label
        self.visited = False

if __name__ == "__main__":
    graph = Graph()
    graph.add_vertex('A')
    graph.add_vertex('B')
    graph.add_edge(0, 1)
    graph.add_vertex('C')
    graph.add_edge(1, 2)
    graph.add_vertex('D')
    graph.add_edge(0, 3)
    graph.add_vertex('E')
    graph.add_edge(0, 4)
    graph.add_vertex('F')
    graph.add_edge(3, 5)
    graph.add_edge(0, 5)
    graph.add_vertex('G')
    graph.add_edge(3, 6)
    graph.add_vertex('H')
    graph.add_edge(3, 7)
    graph.add_vertex('I')
    graph.add_edge(5, 8)
    graph.add_vertex('J')
    graph.add_edge(4, 9)
    print("No. of vertices :", graph.vertex_count)
    graph.display_graph()
    graph.display_edges()
    graph.bfs(3)
