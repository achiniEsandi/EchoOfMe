import pygame
import sys

# --- Initialize ---
pygame.init()
WIDTH, HEIGHT = 640, 480
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Echo of Me")

# --- Constants ---
TILE_SIZE = 32
FPS = 60
speed = 3

# --- Load Assets ---
player_img = pygame.image.load("assets/player.png")
player_img = pygame.transform.scale(player_img, (32, 32))

tileset = pygame.image.load("assets/tileset.png")

# --- Sample Tilemap ---
tilemap = [
    [0, 0, 1, 1, 2, 2, 1, 0, 0, 3, 3, 1, 0, 0, 2, 1, 1, 0, 0, 0],
    [0, 1, 2, 2, 3, 3, 2, 1, 1, 2, 2, 1, 0, 1, 2, 2, 1, 0, 0, 0],
    [1, 2, 3, 3, 3, 3, 3, 2, 2, 3, 3, 2, 1, 2, 3, 3, 2, 1, 0, 0],
    [1, 2, 3, 1, 1, 1, 3, 3, 3, 3, 3, 3, 1, 3, 1, 1, 3, 1, 1, 0],
    [0, 1, 2, 3, 3, 3, 2, 2, 2, 2, 2, 2, 0, 2, 3, 3, 2, 0, 0, 0],
] + [[0]*20 for _ in range(10)]  # fill rest of screen

# --- Memory Objects ---
memories = [
    {"pos": (5, 2), "message": "You remember the warmth of a childhood friend."},
    {"pos": (12, 4), "message": "A moment of quiet under the sky."},
    {"pos": (17, 6), "message": "That rainy evening you felt truly alive."},
]

active_message = None

# --- Player Position ---
player_x = WIDTH // 2
player_y = HEIGHT // 2

# --- Functions ---
def get_tile(tile_index):
    tiles_per_row = tileset.get_width() // TILE_SIZE
    total_tiles = (tileset.get_width() // TILE_SIZE) * (tileset.get_height() // TILE_SIZE)
    if tile_index >= total_tiles:
        tile_index = 0
    x = (tile_index % tiles_per_row) * TILE_SIZE
    y = (tile_index // tiles_per_row) * TILE_SIZE
    return tileset.subsurface((x, y, TILE_SIZE, TILE_SIZE))

def draw_message_box(text):
    font = pygame.font.SysFont("arial", 16)
    padding = 10
    box_width = 400
    box_height = 80
    box_x = (WIDTH - box_width) // 2
    box_y = HEIGHT - box_height - 20

    box_rect = pygame.Rect(box_x, box_y, box_width, box_height)
    pygame.draw.rect(WIN, (30, 30, 30), box_rect)
    pygame.draw.rect(WIN, (200, 200, 200), box_rect, 2)

    rendered = font.render(text, True, (255, 255, 255))
    WIN.blit(rendered, (box_x + padding, box_y + padding))

# --- Game Loop ---
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += speed

    # Keep player on screen
    player_x = max(0, min(WIDTH - TILE_SIZE, player_x))
    player_y = max(0, min(HEIGHT - TILE_SIZE, player_y))

    # Check for memory interaction
    player_tile_x = player_x // TILE_SIZE
    player_tile_y = player_y // TILE_SIZE
    active_message = None
    for memory in memories:
        mem_x, mem_y = memory["pos"]
        if player_tile_x == mem_x and player_tile_y == mem_y:
            active_message = memory["message"]
            break

    # --- Drawing ---
    WIN.fill((0, 0, 0))

    # Draw tilemap
    for row_index, row in enumerate(tilemap):
        for col_index, tile_index in enumerate(row):
            tile = get_tile(tile_index)
            WIN.blit(tile, (col_index * TILE_SIZE, row_index * TILE_SIZE))

    # Draw player
    WIN.blit(player_img, (player_x, player_y))

    # Draw memory message
    if active_message:
        draw_message_box(active_message)

    pygame.display.update()

# --- Quit ---
pygame.quit()
sys.exit()
