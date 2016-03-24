#!/usr/bin/env python

import requests,json

bridgeIP = "192.168.1.72"                    #IP Address of your Bridge
user = "1028d66426293e821ecfd9ef1a0731df"    #Username you generated


r = requests.get("http://"+bridgeIP+"/api/"+user+"/lights/")
data = json.loads(r.text)


for i in data:
 print '"'+data[i]["name"]+'" Is light ID: ',i
