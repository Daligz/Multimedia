import pygame
#colores  
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BROWN = (90, 50, 15)
WHITE = (255,255,255)

COLOR_SKIN = "#ffe7d5"
COLOR_BORDER = "#651c0d";

# Eyes
COLOR_EYE = "#da3e49"
COLOR_EYE_BRIGHTNESS = "#f0dc63";
COLOR_EYE_BRIGHTNESS_BEHIND = "#f17e72";
COLOR_EYE_BRIGHTNESS_TOP = "#fff7f8";
COLOR_EYE_PUPIL = "#6f0a00";

pygame.init() 
WIDTH = 800
HEIGHT = 600
ScreenSize = (WIDTH, HEIGHT)
Screen = pygame.display.set_mode(ScreenSize)
pygame.display.set_caption("Tohru")

# Functions
def printHead():
    pygame.draw.circle(Screen, COLOR_BORDER, (400, 300), 272.5)
    pygame.draw.circle(Screen, COLOR_SKIN, (400, 300), 270)

def printLeftEye():
    # Left eye border
    pygame.draw.circle(Screen, COLOR_BORDER, (250,  250), 61.5)
    # Left eye
    pygame.draw.circle(Screen, COLOR_EYE, (250,  250), 60)
    # Brightness behind eye
    pygame.draw.ellipse(Screen, COLOR_EYE_BRIGHTNESS_BEHIND, [(217, 240), (70, 70)])
    # Brightness eye
    pygame.draw.ellipse(Screen, COLOR_EYE_BRIGHTNESS, [(235, 275), (50, 35)])
    # Brightness top eye
    pygame.draw.circle(Screen, COLOR_EYE_BRIGHTNESS_TOP, (225,  205), 17)
    # Pupil eye
    pygame.draw.ellipse(Screen, COLOR_EYE_PUPIL, [(245, 220), (10, 75)])

def printRightEye():
    # Right eye border
    pygame.draw.circle(Screen, COLOR_BORDER, (530,  250), 61.5)
    # Right eye
    pygame.draw.circle(Screen, COLOR_EYE, (530,  250), 60)
    # Brightness behind eye
    pygame.draw.ellipse(Screen, COLOR_EYE_BRIGHTNESS_BEHIND, [(500, 240), (70, 70)])
    # Brightness eye
    pygame.draw.ellipse(Screen, COLOR_EYE_BRIGHTNESS, [(515, 275), (50, 35)])
    # Brightness top eye
    pygame.draw.circle(Screen, COLOR_EYE_BRIGHTNESS_TOP, (502,  208), 10)
    # Brightness top eye two
    pygame.draw.circle(Screen, COLOR_EYE_BRIGHTNESS_TOP, (542,  195), 5)
    # Pupil eye
    pygame.draw.ellipse(Screen, COLOR_EYE_PUPIL, [(525, 220), (10, 75)])


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
    Screen.fill(WHITE)
    #--Todos los dibujos van después de esta línea

    printHead()
    printLeftEye()
    printRightEye()

    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(60)  # Limitamos a 20 fotogramas por segundo
pygame.quit() 