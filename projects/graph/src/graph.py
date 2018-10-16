"""
Simple graph implementation compatible with BokehGraph class.
"""


class Graph:
    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, a):
        self.vertices[a] = set()
        pass

    def add_edge(self, a, b):
        if(b not in self.vertices):
            print(f"Node {b} is not in vertex")
        else:
            self.vertices[a].add(b)
        pass

    def get_vertices(self):
        print(self.vertices)
        return self.vertices



graph = Graph()  # Instantiate your graph
graph.add_vertex('0')
graph.add_vertex('1')
graph.add_vertex('2')
graph.add_vertex('3')
graph.add_edge('0', '1')
graph.add_edge('0', '3')
graph.add_edge('0', '4')
print(graph.vertices)