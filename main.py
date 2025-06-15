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

# --- Sample Tilemap (each number = tile index from tileset) ---
tilemap = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 2, 2, 2, 2, 1, 0],
    [1, 2, 3, 3, 3, 3, 2, 1],
    [1, 2, 3, 3, 3, 3, 2, 1],  # 🔁 replaced 4s with 3s
    [1, 2, 3, 3, 3, 3, 2, 1],
    [0, 1, 2, 2, 2, 2, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]


# --- Player Position ---
player_x = WIDTH // 2
player_y = HEIGHT // 2

# --- Functions ---
def get_tile(tile_index):
    tiles_per_row = tileset.get_width() // TILE_SIZE
    total_tiles = (tileset.get_width() // TILE_SIZE) * (tileset.get_height() // TILE_SIZE)
    if tile_index >= total_tiles:
        print(f"Tile index {tile_index} is out of range! Max: {total_tiles - 1}")
        tile_index = 0  # fallback to default tile
    x = (tile_index % tiles_per_row) * TILE_SIZE
    y = (tile_index // tiles_per_row) * TILE_SIZE
    return tileset.subsurface((x, y, TILE_SIZE, TILE_SIZE))


# --- Game Loop ---
clock = pygame.time.Clock()
running = True
while running:
    clock.tick(FPS)

    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Movement Input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] or keys[pygame.K_a]:
        player_x -= speed
    if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
        player_x += speed
    if keys[pygame.K_UP] or keys[pygame.K_w]:
        player_y -= speed
    if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        player_y += speed

    # --- Draw Everything ---
    WIN.fill((0, 0, 0))  # Clear screen

    # Draw tilemap
    for row_index, row in enumerate(tilemap):
        for col_index, tile_index in enumerate(row):
            tile = get_tile(tile_index)
            WIN.blit(tile, (col_index * TILE_SIZE, row_index * TILE_SIZE))

    # Draw player
    WIN.blit(player_img, (player_x, player_y))

    pygame.display.update()

# --- Quit ---
pygame.quit()
sys.exit()
