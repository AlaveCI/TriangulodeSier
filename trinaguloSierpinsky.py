import pygame

pygame.init()
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

FONDO = (241, 238, 238)
LINEAS = (96, 249, 14)

def draw_sierpinski(x1, y1, x2, y2, x3, y3, level):
    if level == 0:
        pygame.draw.polygon(screen, LINEAS, [(x1, y1), (x2, y2), (x3, y3)], 1)
    else:
        x12 = (x1 + x2) // 2
        y12 = (y1 + y2) // 2
        x23 = (x2 + x3) // 2
        y23 = (y2 + y3) // 2
        x31 = (x3 + x1) // 2
        y31 = (y3 + y1) // 2

        draw_sierpinski(x1, y1, x12, y12, x31, y31, level - 1)
        draw_sierpinski(x12, y12, x2, y2, x23, y23, level - 1)
        draw_sierpinski(x31, y31, x23, y23, x3, y3, level - 1)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(FONDO)

    x1, y1 = width // 2, 100
    x2, y2 = 100, height - 100
    x3, y3 = width - 100, height - 100

    draw_sierpinski(x1, y1, x2, y2, x3, y3, 6)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
