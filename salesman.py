from dijkstra import dijkstra
from node import Node
import logging
import sys
from optimizer import Optimizer

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)

##TODO: Remember that dicts (edges, nodes, etc) are extracted randomly. Account for this in matrix and lookups. So not by index, but object reference.

## Implements a solution to the travelling salesman problem
def salesman(undirectedgraph, checkpoints):
    print("call to salesman")
    #TODO: Make a distance Dict
    distances = {}
    #TODO: iterate through all to all checkpoints
    for checkpoint in checkpoints:
        print("enter iteration")
        distances[checkpoint[0]] = (checkpoint[1], checkpoint[2])
        for check in checkpoints:
            if check[0] == checkpoint[0]:
                #TODO: is NAN
                print("did nothing")
            else:
                print("made a node")
                #TODO: Make nodes
                #print (checkpoint[1], checkpoint[2], check[1], check[2])
                sourcenode = Node(checkpoint[1], checkpoint[2])
                targetnode = Node(check[1], check[2])
                
                #TODO: calculate shortest path with dijkstra
                pathstack, distancefromsource = dijkstra(undirectedgraph, sourcenode, targetnode)
                
                #TODO: Add to distance dict
                distances[checkpoint[0]][check] = distancefromsource

    #TODO: Thus we optimize
    print ("made it!")
    print (distances)
