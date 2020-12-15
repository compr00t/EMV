import sys
import math

if len(sys.argv) < 2:
	print("Please input a resposne APDU from a GPO as first input!")
else:
	x = str(sys.argv[1]).upper()

	if x.startswith("80"):
		
		x = x.replace(" ", "")
		if x.endswith("9000"):
			x = x[0:-4]

		print("")
		print("[=] -------------------- TLV decoded --------------------")
		print("[=] " + x[0:2] + "[" + x[2:4] + "] Response Message Template Format 1:")
		data = x[4:]
		rounds = math.ceil(len(data)/32)
		for s in range (0, rounds):
			offset = s*32
			print_data = data[(0+offset):(32+offset)]
			print("[=]  " + '{:02d}'.format(s) + ": " + " ".join(print_data[i:i+2] for i in range(0, len(print_data), 2)))
		
		print("")
		print("[=] ---------------- Decode AIP and AFL -----------------")
		print("[=] 82[02]: Application Interchange Profile (AIP):")
		print("[=]  00: " + data[0:2] + " " + data[2:4])

		afl = data[4:]
		print("[=] 94[" + str(int(len(afl)/2)) + "]: Application File Locator (AFL):")
		print("[=]  00: " + " ".join(afl[i:i+2] for i in range(0, len(afl), 2)))

		number_of_sfi = int(len(afl)/8)

		for s in range(0, number_of_sfi):
			offset = s*8
			sfi = int('{0:08b}'.format(int(afl[(0+offset):(2+offset)],16))[0:5],2)
			print("[=]   SFI[" + str(sfi) + "] Start:" + str(int(afl[(2+offset):(4+offset)],16)) + " End:" + str(int(afl[(4+offset):(6+offset)],16)) + " Offline:" + str(int(afl[(6+offset):(8+offset)],16)))

	elif x.startswith("77"):

		x = x.replace(" ", "")
		if x.endswith("9000"):
			x = x[0:-4]

		print("")
		print("[=] -------------------- TLV decoded --------------------")
		print("[=] " + x[0:2] + "[" + x[2:4] + "] Response Message Template Format 2:")
		data = x[4:]
		rounds = math.ceil(len(data)/32)
		for s in range (0, rounds):
			offset = s*32
			print_data = data[(0+offset):(32+offset)]
			print("[=]  " + '{:02d}'.format(s) + ": " + " ".join(print_data[i:i+2] for i in range(0, len(print_data), 2)))
		
		print("")
		print("[=] ------------------- Decode AFL ----------------------")
		afl = ""
		for s in range (0, len(data)):
			if data[s] == "9" and data[(s+1)] == "4" and int(data[(s+2)],16) <= 2:
				afl_length = int(data[s+2:s+4], 16)*2
				afl = data[(s+4):(s+4+afl_length)]
				print("[=] " + data[s:(s+2)] + "[" + data[(s+2):(s+4)] + "] Application File Locator (AFL):")
				print("[=]  00: " + " ".join(afl[i:i+2] for i in range(0, len(afl), 2)))
			s = s+1

		if len(afl) > 7:
			number_of_sfi = int(len(afl)/8)

			for s in range(0, number_of_sfi):
				offset = s*8
				sfi = int('{0:08b}'.format(int(afl[(0+offset):(2+offset)],16))[0:5],2)
				print("[=]   SFI[" + str(sfi) + "] Start:" + str(int(afl[(2+offset):(4+offset)],16)) + " End:" + str(int(afl[(4+offset):(6+offset)],16)) + " Offline:" + str(int(afl[(6+offset):(8+offset)],16)))

		else:
			print("[=] No AFL found in analysed TLV!")

	else:
		print("Can only parse format 1 or 2 TLVs")
