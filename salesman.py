from dijkstra import dijkstra

import logging
import sys

logging.basicConfig(stream=sys.stderr,level=logging.DEBUG)

##TODO: Remember that dicts (edges, nodes, etc) are extracted randomly. Account for this in matrix and lookups. So not by index, but object reference.

## Implements a solution to the travelling salesman problem
def salesman(undirectedgraph, checkpoints):
    n = len(undirectedgraph.nodes)

    # TODO: How to save shortest paths? :/
    shortestPaths = [[float("inf")]*n]*n        # Produce an n*n matrix to store shortest paths between i-node and j-node

    #Lemma 24.17: Predecessor subgraph property: "The predecessor subgraph is a shortest-path tree rooted at s" (Cormen)

    for node in undirectedgraph.nodes:              ## For every node in the graph
        nodedata = dijkstra(undirectedgraph, node)  ## Call dijkstra with the given node as source node. A dict with all nodes and properties
        #nodedata now contains the shortest distances from source node to every other node
        #Is it necessary to call dijkstra more than once (are there several dijkstra shortest-paths?

        for data in nodedata:
            #TODO: How to traverse the shortest path to extract the values
            #Lemma 24.17: Predecessor subgraph property: "The predecessor subgraph is a shortest-path tree rooted at s" (Cormen)
            #So compare the found weight (distance from source) to perhaps other found shortest paths between the same points.
            #Remember unidirectionality.


        print(datanode)


        ## TODO: Use methods in optimizer to find solution to travelling salesman. One must ignore infinities.

    print (shortestPaths)
