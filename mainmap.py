import mapdata
import xml

if __name__ == "__main__":
    xml.etree.ElementTree.parse("roads-approx.xml").findall('WAYPOINTS/POINT')