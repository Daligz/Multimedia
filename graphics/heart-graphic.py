from typing import Sequence
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
 
while not Terminar:
    #---Manejo de eventos
    for Evento in pygame.event.get():
       if Evento.type == pygame.QUIT:
            Terminar = True
    #---La lógica del juego
 

    #---Código de dibujo----
    Pantalla.fill(NEGRO)
    #--Todos los dibujos van después de esta línea
    # Debajo
    # Derecha
    pygame.draw.line(Pantalla, ROJO, (350, 615), (500, 350), SIZE)
    # Izquierda
    pygame.draw.line(Pantalla, ROJO, (170, 350), (500, 800), SIZE)

    # Arriba
    # Derecha
    pygame.draw.arc(Pantalla, ROJO, [(160, 260), (200, 270)], 0.65, 2.8, SIZE)
    # Izquierda
    pygame.draw.arc(Pantalla, ROJO, [(315, 260), (200, 270)], 0.38, 2.5, SIZE)
    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()