try:
    with open("input.txt", "r") as fileContent:
        drawnNumbers = [drawnNumber.strip("\n")
                        for drawnNumber in fileContent.readline().split(",")]
        bingoCards = [line.strip("\n").strip().split() for line in fileContent.readlines()
                      if line.strip("\n")]
        bingoCards = [bingoCards[index:index + 5]
                      for index in range(0, len(bingoCards), 5)]
except FileNotFoundError:
    print("[!] The input file was not found. The program will not continue.")
    exit(-1)


def markDrawnNumbers(drawnNumber, bingoCard):
    for row in bingoCard:
        for index, number in enumerate(row):
            row[index] = "X" if number == drawnNumber else row[index]


def checkIfWon(bingoCard):
    colWon = []
    for index, row in enumerate(bingoCard):
        if row == ["X"] * 5:
            return True
        for col in range(5):
            colWon.append(True if bingoCard[index][col] == "X" else False)
    if not(False in colWon):
        return True
    return False


wonCard = []
wonDrawnNumber = 0
won = False

for drawnNumber in drawnNumbers:
    if won:
        break
    for bingoCard in bingoCards:
        markDrawnNumbers(drawnNumber, bingoCard)
        won = checkIfWon(bingoCard)
        if won:
            wonCard = bingoCard
            wonDrawnNumber = drawnNumber
            break

wonCardUnmarkedNumbers = [
    int(number) for line in wonCard for number in line if number != "X"]

print(sum(wonCardUnmarkedNumbers) * int(wonDrawnNumber))
