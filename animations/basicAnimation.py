import pygame
#colores  
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (90, 50, 15)
WHITE = (255,255,255)

pygame.init()
WIDTH = 800
HEIGHT = 600
ScreenSize = (WIDTH, HEIGHT)
Screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Animacion y Transformaciones")

# Data
posX = WIDTH / 2
posY = HEIGHT / 3
movHor = 0
movVer = 0
direction = "none"

# Functions
def createCubeEntity(surface, x, y, color):
    pygame.draw.rect(surface, color, (x, y, 60, 60))

endGame = False
#Se define para poder gestionar cada cuando se ejecuta un fotograma
reloj = pygame.time.Clock()

while not endGame:
    #---Manejo de Events
    for Event in pygame.event.get():
        if (Event.type == pygame.QUIT):
            endGame = True
        if (Event.type == pygame.KEYDOWN):
            key = Event.key
            if (key == pygame.K_UP):
                direction = "up"
                movVer = -10
            if (key == pygame.K_DOWN):
                direction = "down"
                movVer = 10
            if (key == pygame.K_RIGHT):
                direction = "right"
                movHor = 10
            if (key == pygame.K_LEFT):
                direction = "left"
                movHor = -10
        if (Event.type == pygame.KEYUP):
            key = Event.key
            if (key == pygame.K_UP or key == pygame.K_DOWN):
                direction = "none"
                movVer = 0
            elif (key == pygame.K_RIGHT or key == pygame.K_LEFT):
                direction = "none"
                movHor = 0
    #---La lógica del juego

    #---Código de dibujo----
    Screen.fill(BLACK)
    #--Todos los dibujos van después de esta línea
    posX += movHor
    posY += movVer
    
    createCubeEntity(Screen, posX, posY, WHITE)

    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(60)  # Limitamos a 20 fotogramas por segundo
pygame.quit() 