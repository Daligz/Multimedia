import pygame
import random
#colores
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)
BLANCO = (255,255,255)

pygame.init()
WIDTH = 800
HEIGHT = 600
SIZE = 7
Dimensiones = (WIDTH, HEIGHT)
Pantalla = pygame.display.set_mode(Dimensiones)
pygame.display.set_caption("Introducción a los Gráficos")
 
Terminar = False
#Se define para poder gestionar cada cuando se ejecuta un fotograma
reloj = pygame.time.Clock()

penguin = pygame.image.load("penguin-image.png")
cat = pygame.image.load("cat-image.gif")
dog = pygame.image.load("dog-image.png")

angle = 0
plus = 0
weird = 0

while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
       if Evento.type == pygame.QUIT:
            Terminar = True
    #---La lógica del juego
    plus += 1
    weird += (plus % 10) * 2
    angle = (angle + 0.5) % 360
    #---Código de dibujo----
    Pantalla.fill(NEGRO)
    #--Todos los dibujos van después de esta línea

    # -=======================================================- #
    catRotated = pygame.transform.rotate(cat, angle)
    catRotatedOther = pygame.transform.rotate(cat, weird / 2)

    penguinScaled = pygame.transform.scale(penguin, (weird, 150))
    penguinScaledOther = pygame.transform.scale(penguin, (plus, weird / 2))

    dogFlipped = pygame.transform.flip(dog, True, True)
    # -=======================================================- #

    Pantalla.blit(catRotated, (30, 50))
    Pantalla.blit(catRotatedOther, (50, 120))

    Pantalla.blit(penguinScaled, (1, 5))
    Pantalla.blit(penguinScaledOther, (1, 5))

    Pantalla.blit(dogFlipped, (plus * -1, ((plus * 5) * -1)))
    Pantalla.blit(dog, (angle, angle * (plus)))
    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(75)  # Limitamos a 20 fotogramas por segundo
pygame.quit()