##File that treats all theoretical aspects of map data, not the visualization of it.
## CONTENTS
## - Help method Dijkstras Algorithm
## - Help method Travelling Salesman Problem
## - Class Node
## - Class Edge
## - Class UndirectedGraph

from math import pi,sin, cos, acos


def dijkstra():
    pass

def salesman():
    pass

##Representation of a node (road intersection on a map)
class Node():
    def __init__(self, latitude, longitude):
        self.latitude = latitude        # "x-coordinate"
        self.longitude = longitude      # "y-coordinate"

    def __eq__(self, other):
        if self.latitude == other.latitude and self.longitude == other.longitude:
            return True
        else:
            return False

    def __repr__(self):
        theString = "Latitude:", self.latitude, "Longitude:",self.longitude
        return theString


class Edge():
    def __init__(self, startnode, endnode, wkt):
        self.startnode= startnode #Startpoint already contains coordinates
        self.endnode = endnode #Endpoint already contains coordinates
        self.wkt = wkt
        self.weight = self.calculateTotalEdgeWeight()

    def calculateTotalEdgeWeight(self):
        # For every pair of points in self.wkt, call the following function:
        # TODO: Sett inn variabler som argumenter med koordinater ifra punktparene, loop så lenge det er par igjen, lagre total
        self.distance_on_unit_sphere()

        weight = -1

        return weight

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


    def __eq__(self, other):
        if self.weight == other.weight and self.startnode == other.startnode and self.endnode == other.endnote:
            return True
        else:
            return False

    def __repr__(self):
        theString = "Startnode: " + self.startnode.__repr__() + "   Endnode: " + self.endnode.__repr__() + "  Weight: " + self.weight
        return theString


    def get_distance(self):
        return self.weight

    ##What's this for? What is the property it is referring to?
    def get_property(self):
        pass


class UndirectedGraph():
    def __init__(self):
        pass

    def insert_node(self, node):
        pass

    def delete_node(self, node):
        pass