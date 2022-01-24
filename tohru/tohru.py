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
pygame.display.set_caption("Tohru")

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
    #---La lógica del juego

    #---Código de dibujo----
    Screen.fill(BLACK)
    #--Todos los dibujos van después de esta línea

    #pygame.draw.circle(Screen, WHITE, (400, 100), 75)
    #pygame.draw.rect(Screen, RED, [(350, 175), (100, 200)])

    # Head
    pygame.draw.circle(Screen, BROWN, (400, 300), 270)

    # Left eye
    pygame.draw.circle(Screen, RED, (250,  250), 60)
    # Pupila (Left eye)
    pygame.draw.ellipse(Screen, WHITE, [(235, 225), (20, 75)])

    # Right eye
    pygame.draw.circle(Screen, WHITE, (530,  250), 60)

    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(60)  # Limitamos a 20 fotogramas por segundo
pygame.quit() 