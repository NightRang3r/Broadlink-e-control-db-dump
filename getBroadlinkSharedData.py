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

import base64, sys

try:
    # Python 2.6+
    import json
except ImportError:
    try:
        # from http://code.google.com/p/simplejson
        import simplejson as json
    except ImportError:
        json = None

if json is None:

    def dump_json(x, indent=None):
        """dumb not safe!
        Works for the purposes of this specific script as quotes never
        appear in data set.

        Parameter indent ignored"""
        if indent:
            result = pprint.pformat(x, indent)
        else:
            result = repr(x).replace("'", '"')
        return result

    def load_json(x):
        """dumb not safe! Works for the purposes of this specific script"""
        x = x.replace('\r', '')
        return eval(x)
else:
    dump_json = json.dumps
    load_json = json.loads


IS_PY2 = sys.version_info[0] == 2

def hex2bin(x):
    if IS_PY2:
        return x.decode('hex')
    else:
        return bytes.fromhex(x)


if len(sys.argv) > 1:
    MultipleCode = sys.argv[1]
else:
    MultipleCode = "1"


buttonIDS = []
buttonNames = []


jsonSubIr = open("jsonSubIr").read()
jsonSubIrData = load_json(jsonSubIr)



for i in range(0, len(jsonSubIrData)):
    print("ID:", jsonSubIrData[i]['id'], "| Name:", jsonSubIrData[i]['name'])


choice = input("Select accessory ID: ")
choice = int(choice)

for i in range(0, len(jsonSubIrData)):
    if jsonSubIrData[i]['id'] == choice:
        accessory_name = jsonSubIrData[i]['name']
        print("[+] You selected: ", accessory_name)


jsonButton = open("jsonButton").read()
jsonButtonData = load_json(jsonButton)


for i in range(0, len(jsonButtonData)):
    if jsonButtonData[i]['subIRId'] == choice:
        buttonIDS.append(jsonButtonData[i]['id'])
        buttonNames.append(jsonButtonData[i]['name'])


jsonIrCode = open("jsonIrCode").read()
jsonIrCodeData = load_json(jsonIrCode)


print("[+] Dumping codes to " + accessory_name + ".txt")
codesFile = open(accessory_name + '.txt', 'w')

for i in range(0, len(jsonIrCodeData)):
    for j in range(0, len(buttonIDS)):
        if jsonIrCodeData[i]['buttonId'] == buttonIDS[j]:
            code = ''.join('%02x' % (i & 0xff) for i in jsonIrCodeData[i]['code']) * int(MultipleCode)
            code_bytes = hex2bin(code)
            code_base64 = base64.b64encode(code_bytes)
            code_base64 = code_base64.decode('utf-8')
            result = "Button Name: " + buttonNames[j] + "\r\n" + "Button ID: " + str(jsonIrCodeData[i]['buttonId']) + "\r\n" + "Code: " + code  + "\r\n" + "Base64: " + "\r\n" + code_base64 + "\r\n"
            codesFile.write(result)
