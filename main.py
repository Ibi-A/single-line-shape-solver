class OrientedEdge:
    def __init__(self, origin: int, destination: int) -> None:
        self.origin = origin
        self.destination = destination

    def __str__(self) -> str:
        return f"({self.origin};{self.destination})"


class Graph:

    found_paths = []

    def __init__(
        self,
        remaining_edges: list,
        used_edges: list = None,
        origin_vertex: int = None,
        destination_vertex: int = None,
    ) -> None:
        self.remaining_edges = []
        self.current_path = []
        
        for remaining_edge in remaining_edges:
            self.append_available_edge(remaining_edge)

        if origin_vertex is not None and destination_vertex is not None:
            self.current_path = used_edges
            self.use_edge(origin_vertex, destination_vertex)

    def get_vertices(self):
        vertices_set = set()

        for edge in self.remaining_edges:
            vertices_set.add(edge.origin)
            vertices_set.add(edge.destination)

        for edge in self.current_path:
            vertices_set.add(edge.origin)
            vertices_set.add(edge.destination)

        return list(vertices_set)

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
        self.current_path.append(OrientedEdge(origin_vertex, destination_vertex))

    def get_available_destinations_from_vertex(self, origin_vertex: int) -> list:
        available_destinations = []

        for edge in self.remaining_edges:
            if edge.origin == origin_vertex:
                available_destinations.append(edge.destination)

        return available_destinations

    def get_current_vertex(self):
        return self.current_path[-1].destination

    def find_paths(self):
        solutions = []

        Graph.found_paths = []

        for vertex in self.get_vertices():
            solutions.append(self.iterate(vertex))

        return Graph.found_paths

    def iterate(self, current_vertex: int):
        # get every available destinations from the current vertex
        available_destinations = self.get_available_destinations_from_vertex(
            current_vertex
        )

        if len(available_destinations) == 0 and len(self.remaining_edges) == 0:
            print("----- FOUND PATH -----")
            for e in self.current_path:
                print(str(e))

            print("----------------------")

            # /!\ This part needs to be fixed
            Graph.found_paths.append(self.current_path)

            return None

        # create subgraphs from which we will recursively iterate
        subgraphs = []

        for available_destination in available_destinations:
            remaining_edges = []
            for remaining_edge in self.remaining_edges:
                remaining_edges.append(
                    OrientedEdge(remaining_edge.origin, remaining_edge.destination)
                )

            used_edges = []
            for used_edge in self.current_path:
                used_edges.append(OrientedEdge(used_edge.origin, used_edge.destination))

            subgraphs.append(
                Graph(
                    remaining_edges, used_edges, current_vertex, available_destination
                )
            )

        # iterate recursively on each subgraph
        for subgraph in subgraphs:
            subgraph.iterate(subgraph.get_current_vertex())

        return None




house_edges = [
    # OrientedEdge(1, 2),
    OrientedEdge(2, 3),
    OrientedEdge(2, 4),
    OrientedEdge(3, 4),
    OrientedEdge(3, 5),
    OrientedEdge(3, 6),
    OrientedEdge(4, 5),
    OrientedEdge(4, 6),
    OrientedEdge(5, 6),
]

pyramid_edges = [
    OrientedEdge(1, 2),
    OrientedEdge(1, 3),
    OrientedEdge(2, 3),
    OrientedEdge(2, 4),
    OrientedEdge(2, 5),
    OrientedEdge(2, 6),
    OrientedEdge(3, 5),
    OrientedEdge(3, 6),
    OrientedEdge(3, 7),
    OrientedEdge(4, 5),
    OrientedEdge(5, 6),
    OrientedEdge(6, 7),
]

star_edges = [
    OrientedEdge(1, 2),
    OrientedEdge(1, 12),
    OrientedEdge(2, 3),
    OrientedEdge(2, 4),
    OrientedEdge(2, 12),
    OrientedEdge(3, 4),
    OrientedEdge(4, 5),
    OrientedEdge(4, 6),
    OrientedEdge(5, 6),
    OrientedEdge(6, 7),
    OrientedEdge(6, 8),
    OrientedEdge(7, 8),
    OrientedEdge(8, 9),
    OrientedEdge(8, 10),
    OrientedEdge(9, 10),
    OrientedEdge(10, 11),
    OrientedEdge(10, 12),
    OrientedEdge(11, 12),
]

triangle_edges = [
    OrientedEdge(1, 2),
    OrientedEdge(1, 3),
    OrientedEdge(2, 3)
]

graph = Graph(house_edges)

paths = graph.find_paths()

# print(paths)

for path in paths:
    print("----------------")
    for e in path:
        print(str(e))
    print("----------------")

print(len(paths))