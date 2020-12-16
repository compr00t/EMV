## AFL.py
The response to a GET PROCESSING OPTION (GPO) instruction with or without PDOL can contain the Application File Locator (AFL) that are needed to read specific information from an EMV card. This response GPO can come either in format 1 or format 2. Depending on the format, the AFL are included differently. If a response GPO is inputted into the tool as first parameter, it will detect the proper format and extract and prints all included AFLs. Spaces between the hex chars as well as a tailing Status Word (SW1 / SW2) get stripped automatically:

```
$ AFL.py "80 06 FF FF 08 01 01 00 10 01 01 00 90 00"

[+] -------------------- TLV decoded --------------------
[+] 80[06] Response Message Template Format 1:
[=]  00: FF FF 08 01 01 00 10 01 01 00

[+] ---------------- Decode AIP and AFL -----------------
[+] 82[02]: Application Interchange Profile (AIP):
[=]  00: FF FF
[+] 94[8]: Application File Locator (AFL):
[=]  00: 08 01 01 00 10 01 01 00
[=]   SFI[1] Start:1 End:1 Offline:0
[=]   SFI[2] Start:1 End:1 Offline:0

$ AFL.py "77 0E FF FF FF FF 94 08 08 01 01 01 10 01 01 00 90 00"

[+] -------------------- TLV decoded --------------------
[+] 77[0E] Response Message Template Format 2:
[=]  00: FF FF FF FF 94 08 08 01 01 01 10 01 01 00

[+] ------------------- Decode AFL ----------------------
[+] 94[08] Application File Locator (AFL):
[=]  00: 08 01 01 01 10 01 01 00
[=]   SFI[1] Start:1 End:1 Offline:1
[=]   SFI[2] Start:1 End:1 Offline:0
```

## record.py
If the Application File Locator (AFL) are known, they can be read with a [READ RECORD command APDU](https://cardwerk.com/smart-card-standard-iso7816-4-section-6-basic-interindustry-commands#chap6_5) with instruction `B2` and the targeted SFI and modified start value as first and second parameter. This scripts does the proper modification for the second parameter and generats the corresponding command APDU for this AFL:

```
$ record.py 01 01

[+] +--------------------------------------+
[+] |             Command APDU             |
[+] +-----+-----+----+----+----+------+----+
[+] | CLA | INS | P1 | P2 | Lc | Data | Le |
[+] +-----+-----+----+----+----+------+----+
[+] |  00 |  B2 | 01 | 0c | 00 |      |    |
[+] +-----+-----+----+----+----+------+----+
[+]
[=] 00: 00 B2 01 0C 00
```

## Disclaimer
`EMV` is a trademark of [EMVCo](https://www.emvco.com/) and is used purely for descriptive purposes. These tools are not affiliated with EMVCo. Further, all tools are used at the user's own risk and only for cards with explicit permission of the card issuer.
