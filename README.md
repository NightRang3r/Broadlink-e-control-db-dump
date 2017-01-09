# Description

# econtrol-db-dump.py

This script will "parse" the broadlink e-Control Android application **rmt.db database** and dump the IR / RF codes for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub.

You need to get the "rmt.db" file from your (rooted) android device or emulator (ARM), 

the file is located in "/data/data/com.broadlink.rmt/databases/rmt.db" and put it in the same folder as this script.

<pre> adb pull /data/data/com.broadlink.rmt/databases/rmt.db </pre>

# getBroadlinkSharedData.py

This script will "parse" the broadlink e-Control Android application **"SharedData"** json files and dump the IR / RF codes for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub
NO ROOT ACCESS REQUIRED

Just connect your Android device to your computer and browse the SD card / External Storage folder "/broadlink/newremote/SharedData/"
You need to get the following files:

jsonSubIr
jsonButton
jsonIrCode

and put them in the same folder as this script.

run: python getBroadlinkSharedData.py
