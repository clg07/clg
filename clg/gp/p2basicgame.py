import pygame
import sys

pygame.init()

screen_width = 800
screen_height = 700
screen = pygame.display.set_mode((screen_width, screen_height))

player = pygame.Rect((200, 300, 50, 100))

clock = pygame.time.Clock()

while True:
    screen.fill((0, 0, 0))
    pygame.draw.rect(screen, (255, 0, 0), player)

    # controls
    key = pygame.key.get_pressed()
    if key[pygame.K_UP]:
        player.move_ip(0, -1)
    elif key[pygame.K_DOWN]:
        player.move_ip(0, 1)
    elif key[pygame.K_LEFT]:
        player.move_ip(-1, 0)
    elif key[pygame.K_RIGHT]:
        player.move_ip(1, 0)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    pygame.display.update()
    clock.tick(60)