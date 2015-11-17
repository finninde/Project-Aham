from node import Node

# Creates an undirected graph
class UndirectedGraph():
    def __init__(self):
        self.nodes = set()
        self.edges = {}

    def insert_node(self, node):
        self.nodes.add(node)

    def delete_node(self, node):
        if node in self.nodes:
            self.nodes.remove(node)

    def insert_edge(self, edge):
        # Has startnode been used before?
        if edge.startnode in self.edges:
            # If so, check if a line has been drawn to the endnode
            if edge.endnode not in self.edges[edge.startnode]:
                # If not: add it!
                self.edges[edge.startnode][edge.endnode] = edge

        # If the startnode hasn't been used before, we add it!
        else:
            self.edges[edge.startnode] = {edge.endnode: edge}

        # Since the graph is undirected, we reverse start and end, and run the same checks again!
        temp = edge.startnode
        edge.startnode = edge.endnode
        edge.endnode = temp

        if edge.startnode in self.edges:
            if edge.endnode not in self.edges[edge.startnode]:
                self.edges[edge.startnode][edge.endnode] = edge
        else:
            self.edges[edge.startnode] = {edge.endnode: edge}
