#!/usr/bin/env python

"""
TalkToEagle.py: Example of python code for talk to the Rainforest Automation Eagle.
Written using Python 2.7
Version 1.0, 17JUN2013
"""
__author__      = "Gordon Oliver, Fast Networks Pty Ltd"

import httplib
#import request
import time
import os
import socket
import sys
import time
from xml.etree import ElementTree as ET
from microdotphat import write_string, set_decimal, clear, show







while True:
    try:
        s_watts=""
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        xml_buffer=""
        print s
        # Enter your Eagle's IP below
        Eagle_IP = "xxx.xxx.xxx.xxx"

        s.connect((Eagle_IP, 5002))
        time.sleep(1)
        # spaces and LineFeed charachters are important!!!
        sendstr = "<LocalCommand>\n <Name>list_devices</Name>\n</LocalCommand>\n"
        s.send(sendstr)
        print
        print "sending to Eagle: \n\r"
        sys.stdout.write(sendstr)
        time.sleep(1)
        print

        print "Eagle response: \n\r"

        while 1:
            buf = s.recv(1000)
            if not buf:
                break
            ##sys.stdout.write(buf)

        s.close()
        time.sleep(1)

        print "parse this response and us ethe MACID to request more information\n\r"

        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        print s

        s.connect((Eagle_IP, 5002))
        time.sleep(1)

        # spaces and LineFeed charachters are important!!!  type your MAC ID 0xFFFFFFFFF
        sendstr = '<LocalCommand>\n <Name>get_device_data</Name>\n <MacId>MACID</MacId>\n</LocalCommand>\n'
        s.send(sendstr)

        print
        print "sending to Eagle: \n\r"
        sys.stdout.write(sendstr)
        time.sleep(1)
        file=open("xml_string.xml","w")
        print
        print "Eagle response: \n\r"
        file.write("<Eagle> \n")
        while 1:
            buf = s.recv(1000)
            file.write(buf)
            if not buf:
                break
            xml_buffer=buf
            ##sys.stdout.write(buf)
        file.write("</Eagle> \n")
        file.close()
        time.sleep(1)

        Test_file = open('xml_string.xml','r')
        root = ET.parse(Test_file).getroot()
        Test_file.close()

        for elem in root.iter(tag="Demand"):
                raw_watts=int(elem.text,16)
        for elem in root.iter(tag="Divisor"):
                div=int(elem.text,16)

	clear()
        watts=float(raw_watts)/1000
        print raw_watts
        print watts
        print div
        print "send to Power"
        s_watts=str(watts)
        
        
	write_string(s_watts,kerning=False)
	show()
        s.close()
        time.sleep(60)
    except  KeyboardInterrupt:
        
        break
