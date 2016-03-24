#!/usr/bin/env python

from scapy.all import *
import requests,json

def arp_display(pkt):
  if pkt[ARP].op == 1: #who-has (request)
    if pkt[ARP].psrc == '0.0.0.0': # ARP Probe
      print pkt[ARP].hwsrc

print sniff(prn=arp_display, filter="arp", store=0, count=0)
