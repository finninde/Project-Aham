from optimizer import Optimizer
from node import Node
from edge import Edge
from undirectedgraph import UndirectedGraph
from dijkstra import dijkstra
from salesman import salesman



if __name__ == "__main__":
    node1 = Node(2,1)
    node2 = Node(2,1)

    print(node1.__repr__())
    print(node2.__repr__())
    print(node1.__eq__(node2))