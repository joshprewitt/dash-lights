#!/usr/bin/env python

from scapy.all import *
import requests,json

bridgeIP = "192.168.1.72"                    #IP Address of your Bridge
user = "newdeveloper"    #Username you generated
dashMac = "74:c2:46:5a:57:62"                #MAC address of your Dash button
lightID = "8"                                #ID of the light you want to control

def toggle(lightID):
 url = "http://"+bridgeIP+"/api/"+user+"/lights/"+lightID
 r = requests.get(url)
 data = json.loads(r.text)
 if data["state"]["on"] == False:
  r = requests.put(url+"/state",json.dumps({'on':True}))
 elif data["state"]["on"] == True:
  r = requests.put(url+"/state",json.dumps({'on':False}))

def arp_display(pkt):
 if pkt[ARP].op == 1:
  if pkt[ARP].psrc == '0.0.0.0':
   if pkt[ARP].hwsrc == dashMac:
    toggle(lightID)

print sniff(prn=arp_display, filter="arp", store=0, count=0)
