from optimizer import Optimizer
from node import Node
from edge import Edge
from undirectedgraph import UndirectedGraph
from dijkstra import dijkstra
from salesman import salesman
from mapparser import Mapparser


if __name__ == "__main__":
    mpp = Mapparser('roads-approx.xml')
    waypoints = mpp.getWaypoints()
    patches = mpp.getPatches()
    # Node is waypoints
    graph = UndirectedGraph()
    for node in waypoints:
        graph.insert_node(Node(node[0],node[1]))
    for edge in patches:
        graph.insert_edge(Edge((edge[0], edge[1]), (edge[2], edge[3]), edge[4]))

    salesman(graph)

