import pygame

pygame.init()

# Constants
WIDTH, HEIGHT = 1000, 700
TILE_SIZE = 38
pac_x, pac_y = TILE_SIZE, TILE_SIZE
score = 0
direction = 0  # 1-top, 2-right, 3-bottom, 4-left


# Colors
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


# Maze Layout (1 = Wall, 0 = Chijjee)
maze = [
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 1],
    [1, 0, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 0, 1, 1, 1],
    [1, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
]



def draw_maze():
    for row in range(len(maze)):
        for col in range(len(maze[0])):
            if maze[row][col] == 1:
                pygame.draw.rect(screen, BLUE, (col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE))
            elif maze[row][col] == 0:
                pygame.draw.circle(screen, RED, (col * TILE_SIZE + TILE_SIZE // 2, row * TILE_SIZE + TILE_SIZE // 2), 5)

def show_score():
    score_text = pygame.font.Font(None, 50).render(f"Score: {score}", True, (255, 255, 255))
    screen.blit(score_text, (10, 10))


def is_safe(new_x, new_y):
    col, row = new_x // TILE_SIZE, new_y // TILE_SIZE
    return maze[row][col] != 1

def handle_movement():
     # 1-top, 2-right, 3-bottom, 4-left
    global pac_x, pac_y, score, direction

    if direction == 1:
        if is_safe(pac_x, pac_y-TILE_SIZE):
            pac_y -= TILE_SIZE
    elif direction == 2:
        if is_safe(pac_x+TILE_SIZE, pac_y):
            pac_x += TILE_SIZE
    elif direction == 3:
        if is_safe(pac_x, pac_y+TILE_SIZE):
            pac_y += TILE_SIZE
    elif direction == 4:
        if is_safe(pac_x-TILE_SIZE, pac_y):
            pac_x -= TILE_SIZE

    col, row = pac_x // TILE_SIZE, pac_y // TILE_SIZE

    if maze[row][col] == 0:
        maze[row][col] = 2
        score += 10



# Create Window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Track")



# Main loop
running = True
while running:
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                direction = 4
            elif event.key == pygame.K_RIGHT:
                direction = 2
            elif event.key == pygame.K_DOWN:
                direction = 3
            elif event.key == pygame.K_UP:
                direction = 1

    draw_maze()
    pygame.draw.circle(screen, YELLOW, (pac_x + TILE_SIZE // 2, pac_y + TILE_SIZE // 2), TILE_SIZE // 2)
    show_score()
    handle_movement()

    pygame.display.update()
    pygame.time.delay(400)

pygame.quit()
