##File that treats all theoretical aspects of map data, not the visualization of it.
## CONTENTS
## - Help method Dijkstras Algorithm
## - Help method Travelling Salesman Problem
## - Class Node
## - Class Edge
## - Class UndirectedGraph

from math import pi,sin, cos, acos

## Implements dijkstras algorithm for finding the shortest path in a graph from a given start point to a given end point
def dijkstra():
    pass

## Implements a solution to the travelling salesman problem for a given start node
def salesman():
    pass

## Representation of a node (road intersection on a map)
class Node():
    def __init__(self, latitude, longitude):
        self.latitude = latitude        # "x-coordinate"
        self.longitude = longitude      # "y-coordinate"

    ## Defines how the compiler should check for equality of two instances
    def __eq__(self, other):
        if self.latitude == other.latitude and self.longitude == other.longitude:
            return True
        else:
            return False

    ## Defines how the compiler should print out an object instance
    def __repr__(self):
        theString = "Latitude: " + self.latitude +  "\tLongitude: " + self.longitude
        return theString


## Representation of an edge (road)
class Edge():
    def __init__(self, startnode, endnode, wkt):
        self.startnode= startnode #Startpoint already contains coordinates
        self.endnode = endnode #Endpoint already contains coordinates
        self.wkt = wkt
        self.weight = self.calculateTotalEdgeWeight()

    ## Calculates total road length
    def calculateTotalEdgeWeight(self):
        # For every pair of points in self.wkt, call the following function:
        # TODO: Sett inn variabler som argumenter med koordinater ifra punktparene, loop så lenge det er par igjen, lagre total
        self.distance_on_unit_sphere()

        weight = -1

        return weight


    #Uses trig to find the total road length with respect to the earth's spherical shape.
    def distance_on_unit_sphere(self, lat1= -1, long1= -1, lat2= -1, long2= -1):
        # Source: provided source code from project text
        earth_radius = 6372.8

        degrees_to_radians = pi/180
        phi1 = (90.0 - lat1) * degrees_to_radians
        phi2 = (90.0 - lat2) * degrees_to_radians

        theta1 = long1 * degrees_to_radians
        theta2 = long2 * degrees_to_radians

        cos_val = (sin(phi1)*sin(phi2)*cos(theta1-theta2)) + cos(phi1) * cos(phi2)

        arc_length = acos(cos_val)

        return arc_length*earth_radius


    ## Standard method to define how to check for equality
    def __eq__(self, other):
        if self.weight == other.weight and self.startnode == other.startnode and self.endnode == other.endnote:
            return True
        else:
            return False

    ## Standard method to define how an instance should be printed
    def __repr__(self):
        theString = "Startnode: " + self.startnode.__repr__() + "   Endnode: " + self.endnode.__repr__() + "  Weight: " + self.weight
        return theString

    ## Gets the road length
    def get_distance(self):
        return self.weight

    ##What's this for? What is the property it is referring to?
    ## TODO: Find out if this is necessary
    def get_property(self):
        pass


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
        ##Hvis vi allerede har tegnet en kant ifra startnoden ifra før / finnes nøkkelen til startnode?
        if (edge.startnode.latitude, edge.startnode.longitude) in self.edges:
            ##Sjekk om det har blitt tegnet til samme sluttnode... / om nøkkelen til sluttnode ikke finnes i startnodedict...
            if (edge.endnode.latitude,edge.endnode.longitude) not in self.edges[(edge.startnode.latitude, edge.startnode.longitude)]:
                ##Legg den til!
                self.edges[(edge.startnode.latitude, edge.startnode.longitude)][(edge.endnode.latitude,edge.endnode.longitude)] = edge
        ##Om det ikke finnes et slikt startnodedict...
        else:
            self.edges[(edge.startnode.latitude, edge.startnode.longitude)] = {(edge.endnode.latitude, edge.endnote.longitude): edge}





    def delete_edge(self, edge):
        pass