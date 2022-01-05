import os
import subprocess
from pySMART import Device
from pySMART import DeviceList
import pySMART
import shutil
import psutil

listofdevices = []

print("This will notify you if there are any issues with the drive health or usage summary")

for i in listofdevices:
    if i.smart_enabled == False:
        print("Device does not have smart enabled on it")
        print(i.serial)
        print(i.model)
        print(i.name)
    if i.assessment != "PASS":
        print("Device is not passing SMART assessment")
        print(i.serial)
        print(i.model)
        print(i.name)
    if len(i.messages) != 0:
        for j in i.messages:
            print(j)
            print(i.serial)
            print(i.model)
            print(i.name)

#print(i.temperature)
#    print(i.assessment)
 #   print(i.smart_enabled)
  #  print(i.capacity)
   # print(i.messages)
    #print(i.is_ssd)


#lets get usage summary
for disk in psutil.disk_partitions():
    if disk.fstype:
        if "loop" not in disk.device: #loopfs was the worlds greatest invention
            if psutil.disk_usage(disk.mountpoint).percent > 85:
                print(disk.device, "Usage is over 85%")

for disk in psutil.disk_partitions():
    parts = os.statvfs(disk.mountpoint)
    #print(st.f_files) #inodes total allowed
    #print(st.f_ffree)#inodes free
    if "snap" not in disk.mountpoint:
        if "boot" not in disk.mountpoint:
            if parts.f_files - parts.f_ffree < 1000:
                print(disk.mountpoint, "does not have many more inodes free")

print("If this is the only other message you got then everything seems all good")

