This script will "parse" the broadlink e-Control Android application database and dump the IR / RF codes for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub
You need to get the "rmt.db" file from your (rooted) android device or emulator (ARM), the file is located in "/data/data/com.broadlink.rmt/databases/rmt.db" and put it in the same folder as this script.
adb pull /data/data/com.broadlink.rmt/databases/rmt.db
