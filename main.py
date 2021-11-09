class Edge:
    def __init__(self, vertex_1: int, vertex_2: int) -> None:
        self._vertex_1 = vertex_1
        self._vertex_2 = vertex_2

class Graph:
    def __init__(self, edges: list) -> None:
        self._edges = edges

