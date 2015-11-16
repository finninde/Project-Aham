from dijkstra import dijkstra
from node import Node
import logging
import sys
from optimizer import Optimixer

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)

##TODO: Remember that dicts (edges, nodes, etc) are extracted randomly. Account for this in matrix and lookups. So not by index, but object reference.

## Implements a solution to the travelling salesman problem
def salesman(undirectedgraph, checkpoints):
    #TODO: Make a distance Dict
    distances = {}
    #TODO: iterate through all to all checkpoints
    for checkpoint in checkpoints:
        distances[checkpoint[0]] = (checkpoint[1], checkpoint[2])
        for check in checkpoints:
            if check.get(check[0]):
                #TODO: is NAN
            else:
                #TODO: Make nodes
                sourcenode = Node(checkpoint[1], checkpoint[2])
                targetnode = Node(check[1], check[2])
                
                #TODO: calculate shortest path with dijkstra
                path = dijkstra(undirectedgraph, sourcenode, targetnode)
                distfromsource = path.get(targetnode)[0]
                
                #TODO: Add to distance dict
                distances[chekpoint[0]][check] = distfromsource 

    #TODO: Thus we optimize

