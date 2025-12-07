from AdventDay import AdventDay

class Day6():
    def __init__(self):
        self.day = AdventDay("Day6", "input/day6.txt")
        self.problems = []
        self.bProblems = []
        self.dig0 = []
        self.dig1 = []
        self.dig2 = []
        self.dig3 = []
        self.sign = []
        for i, line in enumerate(self.day.file):
            if(i == 0):
                self.dig0 = line
            elif(i == 1):
                self.dig1 = line
            elif(i == 2):
                self.dig2 = line
            elif(i == 3):
                self.dig3 = line
            elif(i == 4):
                self.sign = line
            else:
                print("Ignoring i = " + str(i))

            index = 0
            for elem in line.split():
                if(index >= len(self.problems)):
                    self.problems.append([])
                self.problems[index].append(elem)
                index += 1

        self.bProblems.append([self.sign[0]])
        for i in range(0, len(self.dig0)):
            if((self.dig0[i] == ' ') and (self.dig1[i] == ' ') and (self.dig2[i] == ' ') and (self.dig3[i] == ' ') and (self.sign[i] == ' ')):
                if(self.sign[i + 1] != ' '):
                    self.bProblems.append([self.sign[i + 1]])
            else:
                digs = [self.dig0[i], self.dig1[i], self.dig2[i], self.dig3[i]]
                self.bProblems[-1].append(0)
                for dig in digs:
                    if dig != ' ' and dig != '\n':
                        self.bProblems[-1][-1] *= 10
                        self.bProblems[-1][-1] += int(dig)

    def getAnswer(self):
        print("Calculating " + self.day.name)
        self.calculateAnswerB()
        print("Done")
        return str(self.day.answer)
    
    def calculateAnswerB(self):
        total = None
        for problem in self.bProblems:
            if problem[0] == '+':
                total = 0
                for num in problem[1:]:
                    total += int(num)
            elif problem[0] == '*':
                total = 1
                for num in problem[1:]:
                    total *= int(num)
            else:
                print("Some Weird sign in table: " + str(problem[0]))
            self.day.answer += total

    def calculateAnswerA(self):
        total = None
        for problem in self.problems:
            if problem[-1] == '+':
                total = 0
                for num in problem[0:-1]:
                    total += int(num)
            elif problem[-1] == '*':
                total = 1
                for num in problem[0:-1]:
                    total *= int(num)
            else:
                print("Some Weird sign in table: " + str(problem[-1]))
            self.day.answer += total

