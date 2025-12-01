from AdventDay import AdventDay

class Day1():
    def __init__(self):
        self.day = AdventDay("Day1", "input/day1.txt")
        self.answer = 0

    def getAnswer(self):
        self.calculateAnswerB()
        return str(self.answer)
    
    def calculateAnswerB(self):
        self.answer = 0
        position = 50
        for line in self.day.file:
            direction = line[0]
            steps = int(line[1:])
            for i in range(0, steps):
                if direction == 'R':
                    position += 1
                    position %= 100
                elif direction == 'L':
                    position -= 1
                    position %= 100
                else:
                    print("Something wrong with direction: " + str(direction))
                if position == 0:
                    self.answer += 1

    def calculateAnswerA(self):
        self.answer = 0
        position = 50
        for line in self.day.file:
            direction = line[0]
            steps = int(line[1:])
            if direction == 'R':
                position += steps
            elif direction == 'L':
                position -= steps
            else:
                print("Something wrong with direction: " + str(direction))
            position %= 100
            if position == 0:
                self.answer += 1
