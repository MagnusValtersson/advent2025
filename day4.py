from AdventDay import AdventDay

class Day4():
    def __init__(self):
        self.day = AdventDay("Day4", "input/day4.txt")
        self.data = []
        for line in self.file:
            self.data.append(list(line))

    def getNeighbors(self, row, col):
        return [[row-1, col-1], [row-1, col], [row-1, col+1], [row, col-1], [row, col+1], [row+1, col-1], [row+1, col], [row+1, col+1]]
    
    def getIfPaperRoll(self, row, col):
        if row < 0 or col < 0 or row >= len(self.data) or col >= len(self.data[0]):
            return False
        if self.data[row][col] == '@':
            return True
        else:
            return False

    def getAnswer(self):
        print("Calculating Day3")
        self.calculateAnswerB()
        print("Done")
        return str(self.day.answer)
    
    def calculateAnswerB(self):
        managedToMove = True
        while managedToMove:
            managedToMove = False
            for row in range(0, len(self.data)):
                for col in range(0, len(self.data[0])):
                    numOfPaperRolls = 0
                    if self.getIfPaperRoll(row, col):
                        neighbors = self.getNeighbors(row, col)
                        for r, c in neighbors:
                            if self.getIfPaperRoll(r, c):
                                numOfPaperRolls += 1
                        if numOfPaperRolls < 4:
                            self.data[row][col] = '.'
                            self.day.answer += 1
                            managedToMove = True
    
    def calculateAnswerA(self):
        for row in range(0, len(self.data)):
            for col in range(0, len(self.data[0])):
                numOfPaperRolls = 0
                if self.getIfPaperRoll(row, col):
                    neighbors = self.getNeighbors(row, col)
                    for r, c in neighbors:
                        if self.getIfPaperRoll(r, c):
                            numOfPaperRolls += 1
                    if numOfPaperRolls < 4:
                        self.day.answer += 1