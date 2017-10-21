# Description

# * All Scripts are written using python 2.7 

# econtrol-db-dump.py

This script will "parse" the broadlink e-Control Android application **rmt.db database** and dump the IR / RF codes (in HEX format) for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub.

You need to get the "rmt.db" file from your android device or emulator (ARM), 

**ROOT ACCESS REQUIRED**

the file is located in "/data/data/com.broadlink.rmt/databases/rmt.db" and put it in the same folder as this script.

<pre> ~# adb pull /data/data/com.broadlink.rmt/databases/rmt.db </pre>

# getBroadlinkSharedData.py

This script will "parse" the broadlink e-Control Android application **"SharedData"** json files and dump the IR / RF codes (in HEX format) for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub

**NO ROOT ACCESS REQUIRED**

Just connect your Android device to your computer and browse the SD card / External Storage folder "/broadlink/newremote/SharedData/"
You need to get the following files:

jsonSubIr

jsonButton

jsonIrCode

and put them in the same folder as this script.

##### *** If you can't find the following files on your phone storage You may need to open the e-control app and on the left side menu choose "Share" and then "Share to other phones in WLAN" it should generate the files. ***

run: `~# python getBroadlinkSharedData.py`

or duplicate code by number

`~# python getBroadlinkSharedData.py 5`

### Requirements

simplejson

`~# pip install simplejson`



# sendCode.py

This is a script you can use to test that your codes are working, It will send the command to the RM Pro
You will need the python-broadlink library for the script to work.


<pre>~# git clone https://github.com/mjg59/python-broadlink.git</pre>

<pre>~# sudo python setup.py install</pre>

You will also need to edit the script `line 6` with your RM Pro IP Address and MAC Address and `line 17` with the code in hex format (Which can be produced by "econtrol-db-dump.py" and "getBroadlinkSharedData.py").


# FOR TC2 RF SWITCHES

In case you get the following error: `Input strings must be a multiple of 16 in length` when sending the TC2 codes you dumped from the DB you will have to do the following:

Try sending the code one time using the "sendCode.py" script:

e.g:
`e90a4200df0909161609160909160916091609160916160909160916091609160916091609161609091609160916160916090916091609160916091616091609160909160916`

If it is not working and you get the `Input strings must be a multiple of 16 in length` error again, try to duplicate it twice:

e.g:
`e90a4200df0909161609160909160916091609160916160909160916091609160916091609161609091609160916160916090916091609160916091616091609160909160916e90a4200df0909161609160909160916091609160916160909160916091609160916091609161609091609160916160916090916091609160916091616091609160909160916`

If not working keep going 3,4,5,6 time until it works with the script.

# broadlink_to_home_assistant_encoder.py

This script will output the codes in a format that will work with home assistant

`~# broadlink_to_home_assistant_encoder.py "packet"`

`~# broadlink_to_home_assistant_encoder.py e90a4200df0909161609160909160916091609160916160909160916091609160916091609161609091609160916160916090916091609160916091616091609160909160916e90a4200df0909161609160909160916091609160916160909160916091609160916091609161609091609160916160916090916091609160916091616091609160909160916`
