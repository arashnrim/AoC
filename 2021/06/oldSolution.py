try:
    with open("input.txt", "r") as fileContent:
        timers = [int(timer)
                  for timer in fileContent.readline() if timer.isdigit()]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)

for _ in range(80):
    new = 0
    for index, timer in enumerate(timers):
        if index > (len(timers) - new - 1):
            break
        timer -= 1
        if timer == -1:
            timers.append(8)
            new += 1
        timers[index] = 6 if timer == -1 else timer

print(len(timers))
