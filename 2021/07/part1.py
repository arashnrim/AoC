try:
    with open("input.txt", "r") as fileContent:
        positions = [int(position)
                     for position in fileContent.readline().split(",")]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")

possibilities = [sum([abs(potentialOutcome - position) for position in positions])
                 for potentialOutcome in range(max(positions))]

print(min(possibilities))
