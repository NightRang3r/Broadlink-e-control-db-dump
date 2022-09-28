import base64, sys, binascii

packet = sys.argv[1]
packet = binascii.unhexlify(packet)
packet = base64.b64encode(packet).decode('utf8')

print(packet)
