try:
    with open("input.txt", "r") as fileContent:
        timers = [int(number) for number in fileContent.readline().split(",")]
        frequencies = [0] * 9
        for timer in timers:
            frequencies[timer] = timers.count(timer)
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)

for _ in range(256):
    newborns, initialSixes = frequencies[-1], frequencies[6]
    for index in range(len(frequencies)):
        if index == 0 and frequencies[index] > 0:
            frequencies[-1] += frequencies[index]
            frequencies[6] += frequencies[index]
            frequencies[index] -= frequencies[index]
        if index < 8:
            if frequencies[6] != initialSixes and index == 5:
                frequencies[index] += initialSixes
                frequencies[index + 1] -= initialSixes
            elif frequencies[-1] != newborns and index == 7:
                frequencies[index] += newborns
                frequencies[index + 1] -= newborns
            else:
                frequencies[index] += frequencies[index + 1]
                frequencies[index + 1] -= frequencies[index + 1]

print(sum(frequencies))
