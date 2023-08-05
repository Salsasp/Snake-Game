import pygame           #OBJECTIVE ----------- MAKE A SNAKE GAME WITH MINIMAL HELP
import point
import grid

#constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
clock = pygame.time.Clock()

velocity = 20
direction = point.Point() #point holds direction in form of -1, 0, or 1

gameGrid = grid.Grid(10)
gameGrid.initGrid()

def drawGrid(gameGrid):
    offset = 10
    xtempPos = offset
    ytempPos = offset
    rectSize = (SCREEN_HEIGHT/gameGrid.getSize())-(offset+1)
    for row in gameGrid.grid:
        for tile in row:
            tile.setRect(rectSize, xtempPos, ytempPos)
            pygame.draw.rect(screen, tile.getColor(), tile.getRect())
            xtempPos += rectSize + offset
        ytempPos += rectSize + offset
        xtempPos = offset
    



running = True
while running:
    screen.fill((0,0,0))
    drawGrid(gameGrid)

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
    pygame.display.update()
    clock.tick(30)

pygame.quit()