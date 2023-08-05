
class Point(object):
    def __init__(self) -> None:
        self.x = 0
        self.y = 0
    def initWithVals(self, x, y):
        self.x = x
        self.y = y
    def setX(self, x):
        self.x = x
    def setY(self, y):
        self.y = y
    def getX(self):
        return self.x
    def getY(self):
        return self.y
    def setXY(self, x, y):
        self.x = x
        self.y = y