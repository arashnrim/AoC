try:
    with open("input.txt", "r") as fileContent:
        depths = [int(depth.strip("\n")) for depth in fileContent.readlines()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")

sums = []

for index in range(len(depths)):
    try:
        def sum(x, y, z): return x + y + z
        sums.append(sum(depths[index], depths[index + 1], depths[index + 2]))
    except IndexError:
        pass

increased = 0
for index in range(len(sums) - 1):
    def isSmaller(a, b): return a < b
    increased += 1 if isSmaller(sums[index], sums[index + 1]) else 0

print(increased)
