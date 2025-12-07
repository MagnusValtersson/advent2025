from AdventDay import AdventDay

class Day7():
    def __init__(self):
        self.day = AdventDay("Day7", "input/day7.txt")
        self.lines = []
        self.openRecursions = 0
        for line in self.day.file:
            self.lines.append(list(line))

    def getAnswer(self):
        print("Calculating " + self.day.name)
        self.calculateAnswerB()
        print("Done")
        return str(self.day.answer)
    
    def continueBeam(self, row, col):
        if(self.openRecursions % 1000000 == 0):
            print(self.openRecursions)
        self.openRecursions += 1
        if self.lines[row][col] == '^':
            self.day.answer += 1
            self.continueBeam(row, col - 1)
            self.continueBeam(row, col + 1)
        else:
            if(row + 1 < len(self.lines)):
                self.continueBeam(row + 1, col)
            else:
                self.openRecursions -= 1

    def calculateAnswerC(self):
        self.day.answer = 1
        self.continueBeam(1, self.lines[0].index('S'))

    def calculateAnswerB(self):
        for row, line in enumerate(self.lines):
            for col, elem in enumerate(line):
                if elem == '.':
                    self.lines[row][col] = 0
        for row, line in enumerate(self.lines[:-1]):
            for col, elem in enumerate(line[:-1]):
                if elem == 'S':
                    self.lines[row + 1][col] = 1
                if(elem != 0) and (elem != 'S') and (elem != '^'):    # if elem is a non-zero number, it is a beam
                    if self.lines[row + 1][col] == '^':
                        self.lines[row + 1][col - 1] += self.lines[row][col]
                        self.lines[row + 1][col + 1] += self.lines[row][col]
                    else:
                        self.lines[row + 1][col] += self.lines[row][col]
        for num in self.lines[-1][:-1]:
            self.day.answer += num

    def calculateAnswerA(self):
        for row, line in enumerate(self.lines[:-1]):
            for col, elem in enumerate(line):
                if elem == 'S':
                    self.lines[row + 1][col] = '|'
                if elem == '|':
                    if self.lines[row + 1][col] == '^':
                        self.day.answer += 1
                        self.lines[row + 1][col - 1] = '|'
                        self.lines[row + 1][col + 1] = '|'
                    else:
                        self.lines[row + 1][col] = '|'

