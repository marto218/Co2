import pygame
import random
import sys

# Inicializar Pygame
pygame.init()

# Configurar pantalla
ANCHO, ALTO = 800, 600
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("¡Recoge las monedas!")

# Colores
BLANCO = (50, 255, 50)
AZUL = (0, 100, 255)
AMARILLO = (255, 0, 0)
NEGRO = (0, 0, 0)
5
# Jugador
jugador_tam = 50
jugador_x = ANCHO // 2
jugador_y = ALTO // 2
velocidad = 6

# Moneda
moneda_tam = 25
moneda_x = random.randint(0, ANCHO - moneda_tam)
moneda_y = random.randint(0, ALTO - moneda_tam)

# Puntuación
puntos = 0
fuente = pygame.font.SysFont("arial", 32)

# Reloj para controlar FPS
reloj = pygame.time.Clock()

# Bucle principal
while True:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and jugador_x > 0:
        jugador_x -= velocidad
    if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - jugador_tam:
        jugador_x += velocidad
    if teclas[pygame.K_UP] and jugador_y > 0:
        jugador_y -= velocidad
    if teclas[pygame.K_DOWN] and jugador_y < ALTO - jugador_tam:
        jugador_y += velocidad

    # Crear rectángulos (para colisiones)
    rect_jugador = pygame.Rect(jugador_x, jugador_y, jugador_tam, jugador_tam)
    rect_moneda = pygame.Rect(moneda_x, moneda_y, moneda_tam, moneda_tam)

    # Detectar colisión
    if rect_jugador.colliderect(rect_moneda):
        puntos += 1
        moneda_x = random.randint(0, ANCHO - moneda_tam)
        moneda_y = random.randint(0, ALTO - moneda_tam)

    # Dibujar
    pantalla.fill(BLANCO)
    pygame.draw.rect(pantalla, AZUL, rect_jugador)
    pygame.draw.rect(pantalla, AMARILLO, rect_moneda)

    # Mostrar puntuación
    texto = fuente.render(f"Basura recogida: {puntos} /15", True, NEGRO)
    pantalla.blit(texto, (10, 10))
    if (puntos== 2): 
        texto = fuente.render(f"¡HAS CONTRARRESTADO TU HUELLA DE CARBONO!", True, NEGRO)
        pantalla.blit(texto, (0, 100))

    # Actualizar pantalla
    pygame.display.flip()
    reloj.tick(60)

