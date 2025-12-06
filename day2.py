from AdventDay import AdventDay

class Day2():
    def __init__(self):
        self.day = AdventDay("Day2", "input/day2.txt")

    def getAnswer(self):
        print("Calculating Day2")
        self.calculateAnswerB()
        print("Done")
        return str(self.day.answer)
    
    def calculateAnswerB(self):
        line = self.day.file.read()
        for ranges in line.split(','):
            bottom, top = ranges.split('-')
            for num in range(int(bottom), int(top) + 1):
                halfLength = int(len(str(num)) / 2)
                # print(num)
                for i in range(1, (halfLength) + 1):
                    if self.checkXS(num, i) == True:
                        self.day.answer += num
                        print(str(num) + " is same when i: " + str(i))
                        break
                # print("\n")
    
    def calculateAnswerA(self):
        line = self.day.file.read()
        for ranges in line.split(','):
            bottom, top = ranges.split('-')
            for num in range(int(bottom), int(top) + 1):
                halfLength = int(len(str(num)) / 2)
                firstHalf = str(num)[0:halfLength]
                secondHalf = str(num)[halfLength:]
                if (firstHalf == secondHalf):
                    self.day.answer += num

    def checkXS(self, num, X):
        isSame = True
        oldI = str(num)[0:X]
        # print("oldI: " + str(oldI))
        i = X
        # print("i: " + str(i))
        # print("len(str(num)): " + str(len(str(num))))
        while i < len(str(num)):
            # print("str(num)[i:i+X]: " + str(num)[i:i+X])
            if str(num)[i:i+X] != oldI:
                isSame = False
            i += X
        return isSame