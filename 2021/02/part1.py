try:
    with open("input.txt", "r") as fileContent:
        movements = [movement.strip("\n").split()
                     for movement in fileContent.readlines()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")

horizontal, depth = 0, 0
for movement in movements:
    match movement[0]:
        case "forward": horizontal += int(movement[1])
        case "up": depth -= int(movement[1])
        case "down": depth += int(movement[1])

print(horizontal * depth)
