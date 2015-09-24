# -*- coding: utf-8 -*-
"""
Created on Thu Sep 24 17:21:15 2015

@author: Yifan
"""



## python get_bus_info.py xxxx-xxxx-xxxx-xxxx-xxxx M7 M7.csv
## api key: c167b534-49d9-414c-a182-6d9631b8ffe5

"""
Assignment 2
"""

import urllib2
import json
import sys
import csv

#key = '0a9caabf-f2c2-4156-b1be-4b2094e77f40'
#bus = 'M7'

if __name__ == '__main__':
    url = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (sys.argv[1], sys.argv[2])

    # = 'http://api.prod.obanyc.com/api/siri/vehicle-monitoring.json?key=%s&VehicleMonitoringDetailLevel=calls&LineRef=%s' % (key, bus)	
    urldata = urllib2.urlopen(url)
    data = json.load(urldata)
    buses = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity']
    
   # file = 'M7.csv'
    with open(sys.argv[3], 'wb') as csvfile:
        writer1 = csv.writer(csvfile)
        header1 = ['Latitude','Longitude','Stop Name','Stop Status']
	  
        writer1.writerow(header1)
        for bus in buses:
            Latitude = bus['MonitoredVehicleJourney']['VehicleLocation']['Latitude']
            Longitude = bus['MonitoredVehicleJourney']['VehicleLocation']['Longitude']
            if bus['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'] == "":
		    Stop_Name = 'NA'
            else: 
	          Stop_Name = bus['MonitoredVehicleJourney']['MonitoredCall']['StopPointName']
            if bus['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance'] == "":
	          Stop_Status = 'NA'
            else:
		    Stop_Status = bus['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance']
            row = [Latitude, Longitude, Stop_Name, Stop_Status]
            writer1.writerow(row)