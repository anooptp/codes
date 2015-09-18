#monitor.py
import urllib
from xml.etree.ElementTree import parse

candidates = ['4384', '4157']
daves_latitude = 41.98062
daves_longitude = -87.668452

def distance(lat1, lat2):
    'Return dist in miles b/w 2 lats'
    return 69 * abs(lat1 - lat2)

def monitor():
    u = urllib.urlopen('http://ctabustracker.com/bustime/map/getBusesForRoute.jsp?route=22')
    doc =  parse(u)

    for bus in doc.findall('bus'):
        busid = bus.findtext('id')
        if busid in candidates:
            lat = float(bus.findtext('lat'))
            dis = distance(lat, daves_latitude)
            print busid, dis, "miles"
    print '-'*10

import time
while True:
    monitor()
    time.sleep(60)
    
