class AdventDay():
    def __init__(self, dayName, inputFileName):
        self.name = dayName
        self.file = open(inputFileName)
        self.answer = 0
 