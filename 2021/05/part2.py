try:
    with open("input.txt", "r") as fileContent:
        segments = [[segment.split(" -> ")]
                    for segment in fileContent.readlines()]
        segments = [tuple([int(axis) for axis in coordinate.strip().split(",")])
                    for segment in segments for coordinates in segment for coordinate in coordinates]
        segments = [segments[index:index + 2]
                    for index in range(0, len(segments), 2)]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)

highestX = 0
highestY = 0

for segment in segments:
    for coordinates in segment:
        x, y = coordinates[0], coordinates[1]
        highestX = x if x > highestX else highestX
        highestY = y if y > highestY else highestY

grid = [[0 for _ in range(highestX + 1)] for _ in range(highestY + 1)]

for segment in segments:
    start, end = segment[0], segment[1]
    x1, y1, x2, y2 = start[0], start[1], end[0], end[1]

    if x1 == x2:
        for row in range(y1 if y1 < y2 else y2, (y2 + 1) if y1 < y2 else (y1 + 1)):
            grid[row][x1] += 1
    elif y1 == y2:
        for col in range(x1 if x1 < x2 else x2, (x2 + 1) if x1 < x2 else (x1 + 1)):
            grid[y1][col] += 1
    else:
        row, col = y1, x1
        while row != (y2 + 1 if y1 < y2 else y2 - 1) and col != (x2 + 1 if x1 < x2 else x2 - 1):
            grid[row][col] += 1
            row -= -1 if y1 < y2 else 1
            col -= -1 if x1 < x2 else 1

dangerousAreas = sum([1 for row in grid for cell in row if cell >= 2])
print(dangerousAreas)
