import pygame           #OBJECTIVE ----------- MAKE A SNAKE GAME WITH MINIMAL HELP
import point
import grid
from collections import deque
import random

#constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800
GRID_WIDTH = 10

#display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

#fundamentals
velocity = 20
direction = point.Point() #point holds direction in form of -1, 0, or 1
direction.setX(1)

#snake
snakePosX = 0
snakePosY = 0
chainLength = 1

#grid
gameGrid = grid.Grid(GRID_WIDTH)
gameGrid.initGrid()
startTile = gameGrid.grid[0][0][0]
prevTile = startTile
gameGrid.grid[0][0][0].setActive(True)

#orb
orbActive = False
orbPos = (0,0)

SPAWN_ORB = pygame.USEREVENT+1
ORB_COLLISION = pygame.USEREVENT+2

def drawGrid(gameGrid):
    offset = 10
    xtempPos = offset
    ytempPos = offset
    rectSize = (SCREEN_HEIGHT/gameGrid.getSize())-(offset+1)
    for row in gameGrid.grid:
        for tile in row:
            tile[0].setRect(rectSize, xtempPos, ytempPos)
            pygame.draw.rect(screen, tile[0].getColor(), tile[0].getRect())
            xtempPos += rectSize + offset
        ytempPos += rectSize + offset
        xtempPos = offset

snakeChain = [startTile]
def moveSnake():
    global snakePosX
    global snakePosY
    global prevTile
    if direction.getX() == 1:
        snakePosX += 1
    if direction.getX() == -1:
        snakePosX -= 1
    if direction.getY() == 1:
        snakePosY += 1
    if direction.getY() == -1:
        snakePosY -= 1
    if snakePosX > GRID_WIDTH -1 or snakePosX < 0 or snakePosY > GRID_WIDTH -1 or snakePosY < 0:
        print("YOU LOSE!")
        return

    for i in range(chainLength):
        gameGrid.grid[snakePosY][snakePosX][0].setActive(True)
        snakeChain.append(gameGrid.grid[snakePosY][snakePosX][0])
        snakeChain[0].setActive(False)
        prevTile = snakeChain[0]
        snakeChain.pop(0)

pygame.time.set_timer(SPAWN_ORB, 10000)
currCircle = 0
running = True
while running:
    screen.fill((0,0,0))
    drawGrid(gameGrid)
    moveSnake()

    key = pygame.key.get_pressed()
    if key[pygame.K_a]:
        direction.setXY(-1, 0)
    if key[pygame.K_w]:
        direction.setXY(0, -1)
    if key[pygame.K_s]:
        direction.setXY(0, 1)
    if key[pygame.K_d]:
        direction.setXY(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == SPAWN_ORB and not orbActive:
            randTile = gameGrid.grid[random.randint(0, GRID_WIDTH-1)][random.randint(0, GRID_WIDTH-1)][0]
            orbActive = True
            orbPos = randTile.getRect().center
            currCircle = pygame.draw.circle(screen, (0,0,255), (randTile.getRect().center), 10)

    if currCircle != 0 and gameGrid.grid[snakePosY][snakePosX][0].getRect().colliderect(currCircle) and orbActive == True:
        snakeChain.append(prevTile)
        currCircle = 0
        orbActive = False
    if currCircle != 0:
        pygame.draw.rect(screen, (0,0,255), currCircle) #TODO: add collision logic for the circles
    
    pygame.display.update()
    #pygame.time.delay(50)
    clock.tick(15)
    

pygame.quit()