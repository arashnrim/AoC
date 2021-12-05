try:
    with open ("input.txt", "r") as fileContent:
        diagnosticBits = [line.strip("\n") for line in fileContent.readlines()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)

def filterBits(remainingBits, bitColumn, searchingFor):
    filteredBits = []

    zeroes, ones = 0, 0
    for diagnosticBit in remainingBits:
        zeroes += 1 if diagnosticBit[bitColumn] == "0" else 0
        ones += 1 if diagnosticBit[bitColumn] == "1" else 0
    for diagnosticBit in remainingBits:
        bitToFilter = ("0" if zeroes > ones else "1") if searchingFor == "oxygen" else ("0" if zeroes <= ones else "1")
        if diagnosticBit[bitColumn] == bitToFilter: filteredBits.append(diagnosticBit)

    return filteredBits[0] if len(filteredBits) == 1 else filterBits(filteredBits, bitColumn + 1, searchingFor)

oxygenResult = filterBits(diagnosticBits, 0, "oxygen")
co2Result = filterBits(diagnosticBits, 0, "C02")

oxygenDecimal, co2Decimal, index = 0, 0, 0
for exponent in range(len(oxygenResult) - 1, -1, -1):
    oxygenDecimal += int(oxygenResult[index]) * (2 ** exponent)
    co2Decimal += int(co2Result[index]) * (2 ** exponent)
    index += 1

print(oxygenDecimal * co2Decimal)
