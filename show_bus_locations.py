# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json
import sys
import urllib2


if __name__=='__main__':
    # key = '0a9caabf-f2c2-4156-b1be-4b2094e77f40'
    # b = 'B52'
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2].upper())
    
    request = urllib2.urlopen(url)
    metadata = json.load(request)
    buses = metadata['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']

    
    print "Bus Line : %s" % (sys.argv[2].upper())
    VehicleActivity = metadata["Siri"]["ServiceDelivery"]["VehicleMonitoringDelivery"][0]["VehicleActivity"]
  
    number = 0
  
    for EachBus in buses:
        latitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Latitude"]
        longitude = EachBus["MonitoredVehicleJourney"]["VehicleLocation"]["Longitude"]
        print "Bus %s is at latitude %s and longitude %s" %(number, latitude, longitude)
        number += 1
    print "Number of Active Buses : %s" %(number)


