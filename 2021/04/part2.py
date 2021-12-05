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


def markDrawnNumbers(drawnNumber, bingoCard):
    for row in bingoCard:
        for index, number in enumerate(row):
            row[index] = "X" if number == drawnNumber else row[index]
    return bingoCard


def checkIfWon(bingoCard):
    for col in range(5):
        colWon = []
        for index, row in enumerate(bingoCard):
            if row == ["X"] * 5:
                return True

            colWon.append(True if bingoCard[index][col] == "X" else False)
        if not(False in colWon) and len(colWon) == 5:
            return True
    return False


wonBingoCards = []
wonCardIndexes = []
wonDrawnNumbers = []
won = False

for drawnNumber in drawnNumbers:
    if len(wonCardIndexes) == len(bingoCards):
        break
    for bingoCardIndex, bingoCard in enumerate(bingoCards):
        won = False
        state = markDrawnNumbers(drawnNumber, bingoCard)
        won = checkIfWon(bingoCard)
        if won and not(bingoCardIndex in wonCardIndexes):
            wonBingoCards.append(state)
            wonCardIndexes.append(bingoCardIndex)
            wonDrawnNumbers.append(drawnNumber)

lastWonBingoCard = wonBingoCards[-1]
lastWonUnmarkedNumbers = sum([int(number) for line in lastWonBingoCard
                              for number in line if number != "X"])
lastWonDrawnNumber = int(wonDrawnNumbers[-1])
print(lastWonUnmarkedNumbers * lastWonDrawnNumber)
