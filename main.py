from optimizer import Optimizer
from node import Node
from edge import Edge
from undirectedgraph import UndirectedGraph
from dijkstra import dijkstra
from salesman import salesman
from mapparser import Mapparser
import logging
import sys
import pickle
from os.path import isfile

logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)

if __name__ == "__main__":
    checkpoints = ((32.542181, -117.029543,),
                    (39.375626, -123.329745),
                    (34.167318, -118.383869),
                    (37.759834, -122.476814),
                    (36.567796, -121.912731),
                    (39.184039, -122.115123),
                    (39.137695, -121.947894)) 
    logging.debug("Main called")

    logging.debug("Creating mapparser to extract data from XML")
    mpp = Mapparser('roads-approx.xml')

    logging.debug("Getting waypoints (nodedata) from XML-file")
    waypoints = mpp.getWaypoints()

    logging.debug("Getting patches (edgedata) from XML-file")
    patches = mpp.getPatches()

    logging.debug("Creating instance of UndirectedGraph")
    graph = UndirectedGraph()

    logging.debug("Inserting all nodes into the undirected graph")
    for node in waypoints:
        graph.insert_node(Node(node[0],node[1]))

    logging.debug("Inserting all edges into the undirected graph")
    for edgedata in patches:
        #Edgedata = [(lat, long), (lat,long), wkt] aka startpoint, endpoint and wkt-data
        graph.insert_edge(Edge(Node(edgedata[0], edgedata[1]), Node(edgedata[2], edgedata[3]), edgedata[4]))

    logging.debug("Calling salesman from main.")
    salesman(graph, checkpoints)

    logging.debug("Call to main ended successfully")

