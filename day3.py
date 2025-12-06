from AdventDay import AdventDay

class Day3():
    def __init__(self):
        self.day = AdventDay("Day3", "input/day3.txt")

    def getAnswer(self):
        print("Calculating Day3")
        self.calculateAnswerB()
        print("Done")
        return str(self.day.answer)
    
    def calculateAnswerB(self):
        for line in self.day.file:
            currentPos = 0
            for i in range(0, 12):
                currentDig = 0
                for j in range(currentPos, (len(line) - (12 - i))):
                    if int(line[j]) > currentDig:
                        currentDig = int(line[j])
                        currentPos = j
                currentPos += 1
                self.day.answer += currentDig * pow(10, (11-i))
    
    def calculateAnswerA(self):
        for line in self.day.file:
            firstPos = 0
            firstDig = 0
            for i in range(0, (len(line) - 2)):
                if int(line[i]) > firstDig:
                    firstDig = int(line[i])
                    firstPos = i
            secondPos = 0
            secondDig = 0
            for i in range(firstPos + 1, (len(line)) - 1):
                if int(line[i]) > secondDig:
                    secondDig = int(line[i])
                    secondPos = i
            self.day.answer += firstDig * 10 + secondDig
