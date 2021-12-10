try:
    with open("input.txt", "r") as fileContent:
        positions = [int(position)
                     for position in fileContent.readline().split(",")]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")

possibilities = []
for potentialOutcome in range(max(positions)):
    total = []
    for position in positions:
        count, value, variablePosition = 1, 0, position
        while variablePosition != potentialOutcome:
            value += count
            variablePosition += 1 if variablePosition < potentialOutcome else -1
            count += 1
        total.append(value)
    possibilities.append(sum(total))

print(min(possibilities))
