import sys

if len(sys.argv) < 3:
	print("Please input an SFI and a start as first and second input!")

else:
	y = int(sys.argv[1])
	x = int(sys.argv[2])

	p1 = format(x, '02x')
	p2 = format((y << 3) + 4, '02x')

	print("[+] +--------------------------------------+")
	print("[+] |             Command APDU             |")
	print("[+] +-----+-----+----+----+----+------+----+")
	print("[+] | CLA | INS | P1 | P2 | Lc | Data | Le |")
	print("[+] +-----+-----+----+----+----+------+----+")
	print("[+] |  00 |  B2 | " + str(p1) + " | " + str(p2) + " | 00 |      |    |")
	print("[+] +-----+-----+----+----+----+------+----+")
	print("[+] ")
	print(("[=] 00: 00 B2 " + str(p1) + " " + str(p2) + " 00").upper())
