from math import pi, sin, cos, acos
from node import Node
from itertools import tee
## Representation of an edge (road)
class Edge():
    def __init__(self, startnode, endnode, wkt):
        self.startnode= startnode #Startpoint already contains coordinates
        self.endnode = endnode #Endpoint already contains coordinates
        self.wkt = wkt
        self.weight = self.calculateTotalEdgeWeight()

    ## Calculates total road length
    ## TODO: NOT FINISHED!
    def calculateTotalEdgeWeight(self):
        # For every pair of points in self.wkt, call the following function:
        # TODO: Sett inn variabler som argumenter med koordinater ifra punktparene, loop så lenge det er par igjen, lagre total

        # Take pairs from list at head  
        (a, b) = tee(self.wkt)
        next(b,None)
        pairs = izip(a,b)
        
        # Pass pairs to distance function
        for pair in pairs:
            self.weight = self.weight + self.distance_on_unit_sphere(pair[0], pair[1])

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
