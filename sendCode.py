import broadlink
import time
import sys

# settings
device = broadlink.rm(host=("10.0.0.2",80), mac=bytearray.fromhex("b4430fffffff"))

print "Connecting to Broadlink device...."
device.auth()
time.sleep(1)
print "Connected...."
time.sleep(1)
device.host

# Replace with your code

codeData = "e90a4200df0909160916091616091609091616091609091616091609160916091609091616090916091616090916091616090916091609161609091616091609160909161609"



device.send_data(codeData.decode('hex'))
print "Code Sent...."