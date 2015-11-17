from queue import PriorityQueue
import itertools
from copy import deepcopy
from node import Node

# Finds shortest path between a source and a target
def dijkstra(undirectedgraph, sourcenode, targetnode):
    # Contains the Dijkstra algorithm output
    nodedata = {}

    #Priorityqueue implemented with dictionaries.
    Q = {}

    def priorityAdd(node, priority):
        if node not in Q.keys():
            Q[node] = priority

    def priorityRemove(node):
        if node in Q.keys():
            del Q[node]

    def priorityUpdate(node, priority):
        priorityRemove(node)
        priorityAdd(node, priority)

    def priorityPop():
        theKey = min(Q, key=Q.get)   # http://stackoverflow.com/questions/3282823/get-key-with-the-least-value-from-a-dictionary
        priorityRemove(theKey)

        return theKey

    for node in undirectedgraph.nodes:
        nodedata[node] = [float("inf"), None] # Distance from source + parent attributes
        priorityAdd(node, float("inf"))          # All nodes are set with priority infinite
    priorityUpdate(sourcenode, 0.0)
    nodedata[sourcenode] = [0, sourcenode]

    while len(Q)>1:
        u = priorityPop()

        if u == (targetnode):    #If we have arrived at the end-node, dijkstra
            break

        if(undirectedgraph.edges.get(u)):
            for v in undirectedgraph.edges[u]:
                if(v in Q.keys() and u != v):
                    w = undirectedgraph.edges[u][v].weight    # Get the weight of the line/road

                    u.d = nodedata[u][0]
                    v.d = Q[v]

                    if v.d > u.d + w:
                        priorityUpdate(v, (u.d+w))        #Update v in the priority queue

                        nodedata[v][0] = u.d + w    #Update v's weight
                        nodedata[v][1] = u          #Update v's parent

    # Now we should have a Dijkstra tree. Crawl from target to source by utilizing the parent attribute.
    # When crawling, add each node to a result stack that shall return the shortest path between
    # target and source. Also include a return with the total distance from target to source

    shortestDistance = nodedata[targetnode][0]
    resultStack = []

    resultStack.append(targetnode)
    closestToTree = resultStack[-1]

    print("CLOSEST TO TREE: ", nodedata[closestToTree][1])

    while nodedata[closestToTree][1] is not sourcenode:  #while we arent at the sourcenode... (only one that shouldnt have parent)

        resultStack.append(nodedata[closestToTree][1])  #add the parent!
        print("Node added to path!")

        closestToTree = resultStack[-1]



    #Return stack with path of nodes sourcenode -> targetnode, float distance to targetnode from source
    return resultStack, shortestDistance
