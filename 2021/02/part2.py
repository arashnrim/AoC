try:
    with open("input.txt", "r") as fileContent:
        movements = [movement.strip("\n").split()
                     for movement in fileContent.readlines()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)

horizontal, depth, aim = 0, 0, 0
for movement in movements:
    match movement[0]:
        case "forward":
            horizontal += int(movement[1])
            depth += aim * int(movement[1])
        case "up": aim -= int(movement[1])
        case "down": aim += int(movement[1])

print(horizontal * depth)
