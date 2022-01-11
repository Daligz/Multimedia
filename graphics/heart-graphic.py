import pygame
import random
#colores  
NEGRO = (0, 0, 0)
ROJO = (255, 0, 0)
CAFE = (90, 50, 15)
BLANCO = (255,255,255)

pygame.init()
Dimensiones = (800, 600)
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
    pygame.draw.line(Pantalla, BLANCO, [400,600], [400, -400], 2)#Vertical
    #--Todos los dibujos van antes de esta línea
    pygame.display.flip()
    reloj.tick(20)  # Limitamos a 20 fotogramas por segundo
pygame.quit()