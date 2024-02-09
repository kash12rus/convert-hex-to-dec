# converting from binary to hex

binaryFile = open("binary.txt", "r")
binaryFile = binaryFile.readlines()
hexFile = open("hex.txt", "w+")

for line in binaryFile:
    binaryCode = line.replace(" ", "")
    hexCode = hex(int(binaryCode, 2))
    hexCode = hexCode.replace("0x", "").upper().zfill(4)
    hexFile.write(hexCode + "\n")

hexFile.close()