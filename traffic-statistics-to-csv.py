#!/usr/bin/env python3

import requests
import xmltodict
import sys
import csv
import datetime

Date = datetime.datetime.utcnow().replace(microsecond=0).isoformat()+"Z"

xml = requests.get("http://192.168.255.1/api/monitoring/traffic-statistics")


pydict = xmltodict.parse(xml.text)

response = pydict['response']


CurrentConnectTime = response['CurrentConnectTime']
CurrentUpload = round((int(response['CurrentUpload'])/(1024**3)), 3)#*10**9			(gigabytes)
CurrentDownload = round((int(response['CurrentDownload'])/(1024**3)), 3)#*10**9		(gigabytes)
CurrentDownloadRate = (int(response['CurrentDownloadRate']))*8						#(bits/s)
CurrentUploadRate = (int(response['CurrentUploadRate']))*8							#(bits/s)
TotalUpload = round((int(response['TotalUpload'])/(1024**3)), 3)#*10**9				(gigabytes)
TotalDownload = round((int(response['TotalDownload'])/(1024**3)), 3)#*10**9			(gigabytes)
TotalConnectTime = response['TotalConnectTime']


# CurrentConnectTime = response['CurrentConnectTime']
# CurrentUpload = response['CurrentUpload']
# CurrentDownload = response['CurrentDownload']
# CurrentDownloadRate = response['CurrentDownloadRate']
# CurrentUploadRate = response['CurrentUploadRate']
# TotalUpload = response['TotalUpload']
# TotalDownload = response['TotalDownload']
# TotalConnectTime = response['TotalConnectTime']

# Make list with the csv field data
entry = [Date, CurrentConnectTime, CurrentUpload, CurrentDownload, CurrentDownloadRate, CurrentUploadRate, TotalUpload, TotalDownload, TotalConnectTime]
# Write into stdout 
with sys.stdout as csvf:
    writer = csv.writer(csvf)
    writer.writerow(entry)
