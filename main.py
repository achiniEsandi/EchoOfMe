import pygame
import sys

# Init
pygame.init()
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echo of Me")

# Load Assets
player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (32, 32))  # Scale to 32x32

# Player Info
player_x, player_y = WIDTH // 2, HEIGHT // 2
speed = 3

# Game Loop
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(60)  # FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player_x -= speed
    if keys[pygame.K_RIGHT]:
        player_x += speed
    if keys[pygame.K_UP]:
        player_y -= speed
    if keys[pygame.K_DOWN]:
        player_y += speed

    # Draw
    WIN.fill((10, 10, 30))  # dark background
    WIN.blit(player_img, (player_x, player_y))
    pygame.display.update()

pygame.quit()
sys.exit()
