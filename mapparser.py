import xml.etree.ElementTree as ET
import re

class Mapparser():
    tree = None
    def __init__(self, filename):
        self.tree = ET.parse(filename)
        self.root = self.tree.getroot()
        self.waypoints = []
        self.patches = []
        
    def calcWaypoints(self):
        for waypoint in self.root.findall('WAYPOINTS/POINT'):
            longtitude = waypoint.find('LONG')
            latitude = waypoint.find('LAT')
            pnt = (float(longtitude.text), float(latitude.text))
            self.waypoints.append(pnt)
    
    def calcPatches(self):
        for patch in self.root.findall('ROADPATCHES/PATCH'):
            startpoint = patch.find('STARTPOINT')
            endpoint = patch.find('ENDPOINT')
            wkt = patch.find('Wkt')
            wkt = re.sub('\)','',
                        (re.sub('LINESTRING \(','',wkt))).split(',')
            wayz = []
            for point in wkt:
                wayz.append(float((point.split(' ')[1]),
                            float(point.split(' ')[0])))
            self.patches.append(float((startpoint.find('LAT').text), 
                                float(startpoint.find('LONG').text), 
                                float(endpoint.find('LAT').text), 
                                float(endpoint.find('LONG').text), 
                                wayz))
    
    def getWaypoints(self):
        return self.waypoints

    def getPatches(self):
        return self.patches


