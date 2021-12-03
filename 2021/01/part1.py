try:
    with open("input.txt", "r") as fileContent:
        depths = [int(depth.strip("\n")) for depth in fileContent.readlines()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")

increased = 0
for index in range(len(depths) - 1):
    def isSmaller(a, b): return a < b
    increased += 1 if isSmaller(depths[index], depths[index + 1]) else 0

print(increased)
