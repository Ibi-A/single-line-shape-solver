class OrientedEdge:
    def __init__(self, origin: int, destination: int) -> None:
        self.origin = origin
        self.destination = destination

    def __str__(self) -> str:
        return f"({self.origin};{self.destination})"


class Graph:
    def __init__(
        self,
        remaining_edges: list,
        used_edges: list = None,
        origin_vertex: int = None,
        destination_vertex: int = None,
    ) -> None:
        self.remaining_edges = []
        self.used_edges = []

        for remaining_edge in remaining_edges:
            self.append_available_edge(remaining_edge)

        if origin_vertex is not None and destination_vertex is not None:
            self.used_edges = used_edges
            self.use_edge(origin_vertex, destination_vertex)

    def append_available_edge(self, edge: OrientedEdge) -> None:
        if self.get_edge_in_remaining_edges(edge.origin, edge.destination) is None:
            self.remaining_edges.append(edge)

        if self.get_edge_in_remaining_edges(edge.destination, edge.origin) is None:
            self.remaining_edges.append(OrientedEdge(edge.destination, edge.origin))

    def remove_available_edge(self, edge: OrientedEdge) -> None:
        self.remaining_edges.remove(
            self.get_edge_in_remaining_edges(edge.origin, edge.destination)
        )
        self.remaining_edges.remove(
            self.get_edge_in_remaining_edges(edge.destination, edge.origin)
        )

    def get_edge_in_remaining_edges(
        self, origin: int, destination: int
    ) -> OrientedEdge:
        for edge in self.remaining_edges:
            if edge.origin == origin and edge.destination == destination:
                return edge

    def use_edge(self, origin_vertex: int, destination_vertex: int) -> None:
        self.remove_available_edge(
            self.get_edge_in_remaining_edges(origin_vertex, destination_vertex)
        )
        self.used_edges.append(OrientedEdge(origin_vertex, destination_vertex))

    def get_available_destinations_from_vertex(self, origin_vertex: int) -> list:
        available_destinations = []

        for edge in self.remaining_edges:
            if edge.origin == origin_vertex:
                available_destinations.append(edge.destination)

        return available_destinations
