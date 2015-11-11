from math import pi,sin, cos, acos

## Creates an undirected graph (read:map)
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
        ## Linje fra AtB
        ##Hvis vi allerede har tegnet en kant ifra startnoden ifra før / finnes nøkkelen til startnode?
        if (edge.startnode.latitude, edge.startnode.longitude) in self.edges:
            ##Sjekk om det har blitt tegnet til samme sluttnode... / om nøkkelen til sluttnode ikke finnes i startnodedict...
            if (edge.endnode.latitude,edge.endnode.longitude) not in self.edges[(edge.startnode.latitude, edge.startnode.longitude)]:
                ##Legg den til!
                self.edges[(edge.startnode.latitude, edge.startnode.longitude)][(edge.endnode.latitude,edge.endnode.longitude)] = edge
        ##Om det ikke finnes et slikt startnodedict...
        else:
            self.edges[(edge.startnode.latitude, edge.startnode.longitude)] = {(edge.endnode.latitude, edge.endnote.longitude): edge}

        ##Reverser start og slutt slik at vi tegner ifra B til A
        temp = edge.startnode
        edge.startnode = edge.endnode
        edge.endnode = temp

        ##Linje fra B til A
        ##Hvis vi allerede har tegnet en kant ifra startnoden ifra før / finnes nøkkelen til startnode?
        if (edge.startnode.latitude, edge.startnode.longitude) in self.edges:
            ##Sjekk om det har blitt tegnet til samme sluttnode... / om nøkkelen til sluttnode ikke finnes i startnodedict...
            if (edge.endnode.latitude,edge.endnode.longitude) not in self.edges[(edge.startnode.latitude, edge.startnode.longitude)]:
                ##Legg den til!
                self.edges[(edge.startnode.latitude, edge.startnode.longitude)][(edge.endnode.latitude,edge.endnode.longitude)] = edge
        ##Om det ikke finnes et slikt startnodedict...
        else:
            self.edges[(edge.startnode.latitude, edge.startnode.longitude)] = {(edge.endnode.latitude, edge.endnote.longitude): edge}