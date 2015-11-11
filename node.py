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