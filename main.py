class Edge:
    def __init__(self, vertex_1: int, vertex_2: int) -> None:
        self.vertex_1 = vertex_1
        self.vertex_2 = vertex_2


class Graph:
    def __init__(self, edges: list) -> None:
        self._edges = edges

    def __init__(
        self, edges: list, origin_vertex: int, destination_vertex: int
    ) -> None:
        self._edges = edges
        self._use_edge(origin_vertex, destination_vertex)

    def get_edge_by_vertices(self, origin_vertex: int, destination_vertex: int) -> Edge:
        found_edge = None

        for edge in self._edges:
            if (
                edge.vertex_1 == origin_vertex and edge.vertex_2 == destination_vertex
            ) or (
                edge.vertex_1 == destination_vertex and edge.vertex_2 == origin_vertex
            ):
                found_edge = edge
                break

        return found_edge

    def _use_edge(self, origin_vertex: int, destination_vertex: int):
        used_edge = self.get_edge_by_vertices(origin_vertex, destination_vertex)
        self._edges.remove(used_edge)
