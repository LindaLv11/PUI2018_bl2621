# -*- coding: utf-8 -*-
"""
Created on Fri Sep 21 18:37:13 2018

@author: 吕柏蓉
"""
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
if not len(sys.argv) == 3:
    print('Invalid number of arguments')
    sys.exit()
    

url = 'http://bustime.mta.info/api/siri/vehicle-monitoring.json?key=' + sys.argv[1]
print(url)
response = urllib.urlopen(url)
data = response.read().decode("utf-8")
data = json.loads(data)
print(type(data))
searchdic = defaultdict(list)
name = sys.argv[2]
count = 0
answer = []
length = len(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'])
for i in range(length):
    newkey = data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['PublishedLineName']
    if newkey == name:
        count += 1
        answer.append(data['Siri']['ServiceDelivery']['VehicleMonitoringDelivery'][0]['VehicleActivity'][i]['MonitoredVehicleJourney']['VehicleLocation'])
print("Bus Line:"+ str(name))
print("Number of Active Buses : " + str(count))
for i in range(count):
    la = str(answer[i]['Latitude'])
    lo = str(answer[i]['Longitude'])
    print("Bus "+ str(i) + " is at latitude "+ la + ' and longitude ' + lo)

