import pygame

class Grid(object):
    def __init__(self, size: int) -> None:
        self.size = size

    def initGrid(self):
        self.grid = [[[Tile((0,0,0), False)]for i in range(self.size)] for j in range(self.size)] #array of tile objects of size "size"

    def getSize(self):
        return self.size

    #def printGrid(self):
    #    for row in self.grid:
    #        print("New Row:")
    #        for tile in row:
    #            tile.printTile()




class Tile(object):
    def __init__(self, color: list, isActive: bool) -> None:
        self.color = color
        self.isActive = isActive

    def setRect(self, size, xpos, ypos):
        self.rect = pygame.Rect((xpos, ypos, size, size))

    def getRect(self):
        return self.rect
    
    def setColor(self, color):
         self.color = color

    def getColor(self):
        return self.color
    
    def setActive(self, state):
        self.isActive = state
        if state == True:
            self.setColor((255,0,0))
        if state == False:
            self.setColor((0,0,0))
            
    def getActive(self):
        return self.isActive

    def printTile(self):
        print(self.color, end=" ")
        print(self.isActive)

