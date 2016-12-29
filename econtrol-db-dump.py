import sqlite3 as lite

# This script will "parse" the broadlink e-Control Android application database and dump the IR / RF codes for selected accessories into a text file which can be later used with broadlink-python to send the codes to the RM PRO hub
# You need to get the "rmt.db" file from your (rooted) android device or emulator (ARM), the file is located in "/data/data/com.broadlink.rmt/databases/rmt.db" and put it in the same folder as this script.
# adb pull /data/data/com.broadlink.rmt/databases/rmt.db

buttonIDS = []
buttonNames = []

# e-Control Database file
con = lite.connect('rmt.db')

# Get All Accessories
with con:
    cur = con.cursor()
    cur.execute("SELECT id, name FROM subIRTable")

    rows = cur.fetchall()

    for row in rows:
        print "Accessory ID: " + str(row[0]) + " | Accessory Name: " + row[1]

# Choose Accessory

accessory = input("Select Accessory ID: ")

cur.execute("SELECT name FROM subIRTable where id =" + str(accessory))

accessory_name = cur.fetchone()[0]

print "[+] You selected: " + accessory_name
print "[+] Dumping codes to " + accessory_name + ".txt"


# Get Buttons id
with con:
    cur = con.cursor()
    cur.execute("SELECT name, id FROM buttonTable where subIRId=" + str(accessory))
    rows = cur.fetchall()

    for row in rows:
        buttonIDS.append(row[1])
        buttonNames.append(row[0])

    codesFile = open(accessory_name + '.txt', 'w')

    # Get Codes

    for i in range(0, len(buttonIDS)):
        cur.execute("SELECT irCode FROM codeTable where buttonId=" + str(buttonIDS[i]))
        code = cur.fetchone()[0]
        result = "Button Name: " + buttonNames[i] + "| Button ID: " + str(buttonIDS[i]) + " | Code: " + str(code).encode('hex') + "\n"
        codesFile.writelines(result.encode('utf-8'))
    codesFile.close()
