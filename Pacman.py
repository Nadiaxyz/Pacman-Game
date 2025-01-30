import pygame
import random
from collections import deque

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 400
GRID_SIZE = 20
GRID_WIDTH = SCREEN_WIDTH // GRID_SIZE
GRID_HEIGHT = SCREEN_HEIGHT // GRID_SIZE
FPS = 10

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)

# Game variables
pacman_pos = [1, 1]
ghost_pos = [5, 5]
dots = [[x, y] for x in range(GRID_WIDTH) for y in range(GRID_HEIGHT) if (x, y) != (1, 1) and (x, y) != (5, 5)]
score = 0
ghost_tick_delay = 3  # Slightly faster ghost movement
ghost_tick_counter = 0

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pac-Man")

def draw_grid():
    for x in range(GRID_WIDTH):
        for y in range(GRID_HEIGHT):
            rect = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(screen, BLACK, rect, 1)

def draw_pacman():
    pacman_rect = pygame.Rect(pacman_pos[0] * GRID_SIZE, pacman_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, YELLOW, pacman_rect)

def draw_ghost():
    ghost_rect = pygame.Rect(ghost_pos[0] * GRID_SIZE, ghost_pos[1] * GRID_SIZE, GRID_SIZE, GRID_SIZE)
    pygame.draw.rect(screen, RED, ghost_rect)

def draw_dots():
    for dot in dots:
        dot_rect = pygame.Rect(dot[0] * GRID_SIZE + GRID_SIZE // 4, dot[1] * GRID_SIZE + GRID_SIZE // 4, GRID_SIZE // 2, GRID_SIZE // 2)
        pygame.draw.rect(screen, WHITE, dot_rect)

def move_ghost_towards_pacman():
    queue = deque([(ghost_pos[0], ghost_pos[1])])
    visited = set()
    visited.add((ghost_pos[0], ghost_pos[1]))
    parent = {}
    while queue:
        current = queue.popleft()
        if current == tuple(pacman_pos):
            break
        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            neighbor = (current[0] + dx, current[1] + dy)
            if (
                0 <= neighbor[0] < GRID_WIDTH and
                0 <= neighbor[1] < GRID_HEIGHT and
                neighbor not in visited and
                neighbor not in dots
            ):
                queue.append(neighbor)
                visited.add(neighbor)
                parent[neighbor] = current
    if tuple(pacman_pos) in parent:
        path = []
        current = tuple(pacman_pos)
        while current != tuple(ghost_pos):
            path.append(current)
            current = parent[current]
        path.reverse()
        if path:
            ghost_pos[0], ghost_pos[1] = path[0]

def main():
    global pacman_pos, ghost_pos, dots, score, ghost_tick_counter
    clock = pygame.time.Clock()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and pacman_pos[0] > 0:
            pacman_pos[0] -= 1
        if keys[pygame.K_RIGHT] and pacman_pos[0] < GRID_WIDTH - 1:
            pacman_pos[0] += 1
        if keys[pygame.K_UP] and pacman_pos[1] > 0:
            pacman_pos[1] -= 1
        if keys[pygame.K_DOWN] and pacman_pos[1] < GRID_HEIGHT - 1:
            pacman_pos[1] += 1
        if pacman_pos in dots:
            dots.remove(pacman_pos)
            score += 1
        if not dots:
            print("You Win! Your score:", score)
            running = False
        ghost_tick_counter += 1
        if ghost_tick_counter >= ghost_tick_delay:
            move_ghost_towards_pacman()
            ghost_tick_counter = 0
        if pacman_pos == ghost_pos:
            print("Game Over! Your score:", score)
            running = False
        screen.fill(BLACK)
        draw_grid()
        draw_pacman()
        draw_ghost()
        draw_dots()
        pygame.display.flip()
        clock.tick(FPS)
    pygame.quit()

if __name__ == "__main__":
    main()
