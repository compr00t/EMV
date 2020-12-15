import sys

y = int(sys.argv[1])
x = int(sys.argv[2])

p1 = format(x, '02x')
p2 = format((y << 3) + 4, '02x')
print(("00 B2 " + str(p1) + " " + str(p2) + " 00").upper())
