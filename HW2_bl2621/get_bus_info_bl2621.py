# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:37:13 2018

@author: 吕柏蓉
"""
from __future__ import print_function
import pandas as pd
import pylab as pl
import os
import json
from collections import defaultdict
try:
    import urllib2 as urllib
except ImportError:
    import urllib.request as urllib
import requests
import sys
#%pylab inline
pl.rc('font', size=15)
if not len(sys.argv) == 4:
    print('Invalid number of arguments')
    sys.exit()
    
fout = open(sys.argv[3], "w")
fout.write('Latitude,Longitude,Stop Name,Stop Status\n')
url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1]
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
print(type(data))
searchdic = defaultdict(list)
name = sys.argv[2]
count = 0
length = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
for i in range(length):
    newkey = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['PublishedLineName']
    if newkey == name:
        count += 1
        try:
            fout.write(str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Latitude']))
        except KeyError:
            fout.write('N/A')
        fout.write(',')
        try:
            fout.write(str(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation']['Longitude']))
        except KeyError:
            fout.write('N/A')        
        fout.write(',')
        try:
            fout.write(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['StopPointName'])
        except KeyError:
            fout.write('N/A')           
        fout.write(',')
        try:        
            fout.write(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['MonitoredCall']['Extensions']['Distances']['PresentableDistance'])
        except KeyError:
            fout.write('N/A')        
        fout.write('\n')

fout.close()
