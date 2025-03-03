import pygame
import random

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 500, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Dodge the Blocks")

# Colors
WHITE = (255, 255, 255)
RED = (200, 0, 0)
BLUE = (0, 0, 255)

# Player attributes
player_size = 50
player_x = WIDTH // 2 - player_size // 2
player_y = HEIGHT - player_size - 10
player_speed = 7

# Block attributes
block_width = 50
block_height = 50
block_speed = 5
blocks = []

# Font setup
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
score = 0
running = True

def create_block():
    x = random.randint(0, WIDTH - block_width)
    y = -block_height
    return [x, y]

# Game loop
while running:
    screen.fill(WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    # Move player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_x > 0:
        player_x -= player_speed
    if keys[pygame.K_RIGHT] and player_x < WIDTH - player_size:
        player_x += player_speed
    
    # Add new blocks
    if random.randint(1, 30) == 1:
        blocks.append(create_block())
    
    # Move blocks
    for block in blocks[:]:
        block[1] += block_speed
        if block[1] > HEIGHT:
            blocks.remove(block)
            score += 1  # Increase score for dodging
        if player_x < block[0] < player_x + player_size or player_x < block[0] + block_width < player_x + player_size:
            if player_y < block[1] + block_height and player_y + player_size > block[1]:
                running = False  # Game over
    
    # Draw player
    pygame.draw.rect(screen, BLUE, (player_x, player_y, player_size, player_size))
    
    # Draw blocks
    for block in blocks:
        pygame.draw.rect(screen, RED, (block[0], block[1], block_width, block_height))
    
    # Display score
    text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(text, (10, 10))
    
    pygame.display.flip()
    clock.tick(30)

pygame.quit()
