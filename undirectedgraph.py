# Creates an undirected graph
class UndirectedGraph():
    def __init__(self):
        self.nodes = {}
        self.edges = {}

    def insert_node(self, node):
        if (node.latitude,node.longitude) not in self.nodes:
            self.nodes[(node.latitude, node.longitude)] = node

    def delete_node(self, node):
        if (node.latitude, node.longitude) in self.nodes:
            del self.nodes[(node.latitude, node.longitude)]

    def insert_edge(self, edge):
        # Has startnode been used before?
        if (edge.startnode.latitude, edge.startnode.longitude) in self.edges:
            # If so, check if a line has been drawn to the endnode
            if (edge.endnode.latitude, edge.endnode.longitude) not in self.edges[(edge.startnode.latitude, edge.startnode.longitude)]:
                # If not: add it!
                self.edges[(edge.startnode.latitude, edge.startnode.longitude)][(edge.endnode.latitude,edge.endnode.longitude)] = edge

        # If the startnode hasn't been used before, we add it!
        else:
            self.edges[(edge.startnode.latitude, edge.startnode.longitude)] = {(edge.endnode.latitude, edge.endnode.longitude): edge}

        # Since the graph is undirected, we reverse start and end, and run the same checks again!
        temp = edge.startnode
        edge.startnode = edge.endnode
        edge.endnode = temp

        if (edge.startnode.latitude, edge.startnode.longitude) in self.edges:
            if (edge.endnode.latitude,edge.endnode.longitude) not in self.edges[(edge.startnode.latitude, edge.startnode.longitude)]:
                self.edges[(edge.startnode.latitude, edge.startnode.longitude)][(edge.endnode.latitude,edge.endnode.longitude)] = edge
        else:
            self.edges[(edge.startnode.latitude, edge.startnode.longitude)] = {(edge.endnode.latitude, edge.endnode.longitude): edge}
