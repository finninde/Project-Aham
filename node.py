## Representation of a node (road intersection on a map)
class Node():
    def __init__(self, latitude, longitude):
        self.latitude = latitude        # "x-coordinate"
        self.longitude = longitude      # "y-coordinate"

    ## Defines how the compiler should check for equality of two instances
    def __eq__(self, other):
        #If coordinates are an exact match (currently no leeway), we assume the nodes to be identical
        if self.latitude == other.latitude and self.longitude == other.longitude:
            return True
        #Elsewise, we assume the nodes (road intersections) to be different
        else:
            return False

    ## Defines how the compiler should display the instance contents as a string
    def __repr__(self):
        theString = "NODEDATA\n" + "Latitude:\t" + str(self.latitude) +  "\t\tLongitude:\t" + str(self.longitude) + "\n\n"
        return theString