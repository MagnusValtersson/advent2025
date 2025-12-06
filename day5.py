from AdventDay import AdventDay

class Day5():
    def __init__(self):
        self.day = AdventDay("Day5", "input/day5.txt")
        self.ranges = []
        self.ids = []
        for line in self.day.file:
            if '-' in line:
                lower, upper = line.split('-')
                self.ranges.append([int(lower), int(upper)])
            else:
                try:
                    self.ids.append(int(line))
                except:
                    print("Ignoring: " + str(line))

    def adjustRangeInRange(self, index, lower, upper):
        newLow, newUpp = self.ranges[index]
        if((newLow >= lower) and (newLow <= upper)):
            if(newUpp <= upper):
                self.ranges[index] = [0, 0]
                return
            else:
                self.ranges[index][0] = upper + 1
        if((newUpp >= lower) and (newUpp <= upper)):
            if(newLow >= lower):
                self.ranges[index] = [0, 0]
                newUpp = 0
            else:
                self.ranges[index][1] = lower - 1

    def isIdInRange(self, id, lower, upper):
        if((id >= lower) and (id <= upper)):
            return True
        else:
            return False

    def getAnswer(self):
        print("Calculating Day3")
        self.calculateAnswerB()
        print("Done")
        return str(self.day.answer)
    
    def calculateAnswerB(self):
        for i in range(0, len(self.ranges)):
            print(self.ranges[i])
            for j in range(0, len(self.ranges)):
                if i != j:
                    lower, upper = self.ranges[j]
                    self.adjustRangeInRange(i, lower, upper)
            if(self.ranges[i] != [0, 0]):
                self.day.answer += self.ranges[i][1] - self.ranges[i][0] + 1


    def calculateAnswerA(self):
        for id in self.ids:
            isFresh = False
            i = 0
            while((isFresh == False) and (i < len(self.ranges))):
                lower, upper = self.ranges[i]
                isFresh = self.isIdInRange(id, lower, upper)
                i += 1
            if(isFresh):
                self.day.answer += 1
