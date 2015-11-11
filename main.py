from optimizer import Optimizer
from node import Node
from edge import Edge
from undirectedgraph import UndirectedGraph
from dijkstra import dijkstra
from salesman import salesman



if __name__ == "__main__":
    graph = UndirectedGraph()
    graph.insert_node(Node(1,2))
    graph.insert_node(Node(1,2))

    salesman(graph) 

