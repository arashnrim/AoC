try:
    with open ("input.txt", "r") as fileContent:
        diagnosticBits = [line.strip("\n") for line in fileContent.readlines()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)

gamma, epsilon = "", ""

for index in range(len(diagnosticBits[0])):
    zeroes, ones = 0, 0
    for diagnosticBit in diagnosticBits:
        zeroes += 1 if diagnosticBit[index] == "0" else 0
        ones += 1 if diagnosticBit[index] == "1" else 0
    if ones > zeroes:
        gamma += "1"
        epsilon += "0"
    elif zeroes > ones:
        gamma += "0"
        epsilon += "1"

gammaDecimal, epsilonDecimal, index = 0, 0, 0

for exponent in range(len(gamma) - 1, -1, -1):
    gammaDecimal += int(gamma[index]) * (2 ** exponent)
    epsilonDecimal += int(epsilon[index]) * (2 ** exponent)
    index += 1

print(gammaDecimal * epsilonDecimal)
