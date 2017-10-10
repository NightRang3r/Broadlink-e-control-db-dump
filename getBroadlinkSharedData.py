# -*- coding: utf-8 -*-

'''
This script will "parse" the broadlink e-Control Android application "SharedData" json files and dump the IR / RF codes for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub
NO ROOT ACCESS REQUIRED

Just connect your Android device to your computer and browse the SD card / External Storage folder "/broadlink/newremote/SharedData/"
You need to get the following files:

jsonSubIr
jsonButton
jsonIrCode

and put them in the same folder as this script.

run: python getBroadlinkSharedData.py 

or duplicate code by number

python getBroadlinkSharedData.py 5

'''

import simplejson as json
import base64, sys


if len(sys.argv) > 1:
    MultipleCode = sys.argv[1]
else:
    MultipleCode = "1"


buttonIDS = []
buttonNames = []


jsonSubIr = open("jsonSubIr").read()
jsonSubIrData = json.loads(jsonSubIr)


for i in range(0, len(jsonSubIrData)):
    print "ID:", jsonSubIrData[i]['id'], "| Name:", jsonSubIrData[i]['name']


choice = input("Select accessory ID: ")

for i in range(0, len(jsonSubIrData)):
    if jsonSubIrData[i]['id'] == choice:
        accessory_name = jsonSubIrData[i]['name']
        print "[+] You selected: ", accessory_name


jsonButton = open("jsonButton").read()
jsonButtonData = json.loads(jsonButton)


for i in range(0, len(jsonButtonData)):
    if jsonButtonData[i]['subIRId'] == choice:
        buttonIDS.append(jsonButtonData[i]['id'])
        buttonNames.append(jsonButtonData[i]['name'])


jsonIrCode = open("jsonIrCode").read()
jsonIrCodeData = json.loads(jsonIrCode)


print "[+] Dumping codes to " + accessory_name + ".txt"
codesFile = open(accessory_name + '.txt', 'w')

for i in range(0, len(jsonIrCodeData)):
    for j in range(0, len(buttonIDS)):
        if jsonIrCodeData[i]['buttonId'] == buttonIDS[j]:
            code = ''.join('%02x' % (i & 0xff) for i in jsonIrCodeData[i]['code']) * int(MultipleCode)
            code_base64 = code.decode("hex").encode("base64")
            result = "Button Name: " + buttonNames[j] + "\r\n" + "Button ID: " + str(jsonIrCodeData[i]['buttonId']) + "\r\n" + "Code: " + code  + "\r\n" + "Base64: " + "\r\n" + code_base64 + "\r\n"
            codesFile.writelines(result.encode('utf-8'))