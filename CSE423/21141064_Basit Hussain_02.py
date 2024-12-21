import pygame 
import random
import sys

# Initialize Pygame
pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Shoot The Circles!")

WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLACK = (0, 0, 0)
TEAL = (0, 255, 255)
AMBER = (255, 191, 0)

# Spaceship (shooter) settings
spaceship_width = 60
spaceship_height = 30
spaceship_x = WIDTH // 2 - spaceship_width // 2
spaceship_y = HEIGHT - 40
spaceship_speed = 8


projectile_radius = 5
projectiles = []


circle_radius = 20
circle_base_speed = 1
circles = []
max_circles = 1  

# Game state variables
score = 0
missed_circles = 0  
max_missed_circles = 3 
mp = 0
mxmp = 3
game_over = False
paused = False
clock = pygame.time.Clock()

# Function to draw a line using the Midpoint Line Algorithm
def draw_line_midpoint(x1, y1, x2, y2, color):
    dx = abs(x2 - x1)
    dy = abs(y2 - y1)
    sx = 1 if x1 < x2 else -1
    sy = 1 if y1 < y2 else -1
    err = dx - dy

    while True:
        pygame.draw.rect(screen, color, (x1, y1, 1, 1))
        if x1 == x2 and y1 == y2:
            break
        e2 = err * 2
        if e2 > -dy:
            err -= dy
            x1 += sx
        if e2 < dx:
            err += dx
            y1 += sy

# Function to draw a circle using the Midpoint Circle Algorithm
def draw_circle_midpoint(xc, yc, r, color):
    x = r
    y = 0
    d = 1 - r
    while x >= y:
        plot_circle_points(xc, yc, x, y, color)
        y += 1
        if d < 0:
            d += 2 * y + 1
        else:
            x -= 1
            d += 2 * (y - x) + 1

def plot_circle_points(xc, yc, x, y, color):
    points = [
        (xc + x, yc + y), (xc - x, yc + y),
        (xc + x, yc - y), (xc - x, yc - y),
        (xc + y, yc + x), (xc - y, yc + x),
        (xc + y, yc - x), (xc - y, yc - x)
    ]
    for px, py in points:
        pygame.draw.rect(screen, color, (px, py, 1, 1))

# Function to draw spaceship using Midpoint Line Algorithm
def draw_spaceship(x, y):
    draw_line_midpoint(x + spaceship_width // 2, y, x, y + spaceship_height, WHITE)
    draw_line_midpoint(x + spaceship_width // 2, y, x + spaceship_width, y + spaceship_height, WHITE)
    draw_line_midpoint(x + spaceship_width // 4, y + spaceship_height, x + spaceship_width // 4, y + spaceship_height + 10, WHITE)
    draw_line_midpoint(x + 3 * spaceship_width // 4, y + spaceship_height, x + 3 * spaceship_width // 4, y + spaceship_height + 10, WHITE)
    draw_line_midpoint(x + spaceship_width // 4, y + spaceship_height + 10, x + 3 * spaceship_width // 4, y + spaceship_height + 10, WHITE)

# Function to draw projectiles
def draw_projectiles():
    for projectile in projectiles:
        draw_circle_midpoint(projectile["x"], projectile["y"], projectile_radius, WHITE)

# Function to draw falling circles
def draw_circles():
    for circle in circles:
        draw_circle_midpoint(circle["x"], circle["y"], circle_radius, WHITE)

# Function to handle projectile and circle collision
def detect_collision(circle, projectile):
    dx = circle["x"] - projectile["x"]
    dy = circle["y"] - projectile["y"]
    distance = (dx**2 + dy**2)**0.5
    return distance <= circle_radius + projectile_radius

# Function to detect collision between spaceship and circle
def detect_spaceship_collision(circle):
    dx = circle["x"] - (spaceship_x + spaceship_width // 2)
    dy = circle["y"] - (spaceship_y + spaceship_height // 2)
    distance = (dx**2 + dy**2)**0.5
    return distance <= circle_radius + spaceship_height // 2

# Function to display the game-over message
def game_over_message():
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over", True, RED)
    screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Function to draw left arrow button using Midpoint Line Algorithm
def draw_left_arrow(x, y, size, color):
    draw_line_midpoint(x + size, y, x, y + size // 2, color)  
    draw_line_midpoint(x, y + size // 2, x + size, y + size, color)  

# Function to draw play/pause button
def draw_play_pause(x, y, size, color, is_paused):
    if is_paused:
        draw_line_midpoint(x, y, x, y + size, color)
        draw_line_midpoint(x, y, x + size, y + size // 2, color)
        draw_line_midpoint(x + size, y + size // 2, x, y + size, color)
    else:
        draw_line_midpoint(x, y, x, y + size, color)
        draw_line_midpoint(x + size, y, x + size, y + size, color)

# Function to draw the red cross button using Midpoint Line Algorithm
def draw_cross(x, y, size, color):
    draw_line_midpoint(x, y, x + size, y + size, color)
    draw_line_midpoint(x + size, y, x, y + size, color)

    
# Main game loop
def game_loop():
    global spaceship_x, projectiles, circles, score, missed_circles, game_over, paused, circle_base_speed, max_circles, misfires, mp, mxmp

    running = True
    while running:
        screen.fill(BLACK)

        # Handle events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Restart button (teal arrow)
                if 10 <= mouse_x <= 40 and 10 <= mouse_y <= 40:
                    score = 0
                    missed_circles = 0
                    misfires = 0
                    circles.clear()
                    projectiles.clear()
                    circle_base_speed = 1
                    max_circles = 1
                    game_over = False
                    print("Starting Over")
                # Play/Pause button (amber, center)
                if 400 <= mouse_x <= 440 and 10 <= mouse_y <= 40:
                    paused = not paused
                # Exit button (red, right)
                if 760 <= mouse_x <= 790 and 10 <= mouse_y <= 40:
                    print(f"Goodbye! Final Score: {score}")
                    pygame.quit()
                    sys.exit()

        # Check if the game is paused
        if not paused and not game_over:
            # Keyboard input for spaceship movement
            keys = pygame.key.get_pressed()
            if keys[pygame.K_a] and spaceship_x > 0:  
                spaceship_x -= spaceship_speed
            if keys[pygame.K_d] and spaceship_x < WIDTH - spaceship_width:  
                spaceship_x += spaceship_speed
            if keys[pygame.K_SPACE]:  
                if len(projectiles) < 5: 
                    projectiles.append({"x": spaceship_x + spaceship_width // 2, "y": spaceship_y})

            # Update projectiles
            for projectile in projectiles[:]:
                projectile["y"] -= 10  
                if projectile["y"] < 0:
                    projectiles.remove(projectile)
            # Update circles
            for circle in circles[:]:
                circle["y"] += circle["speed"]  
                if circle["y"] > HEIGHT:  
                    missed_circles += 1
                    circles.remove(circle)  
                    if missed_circles >= max_missed_circles:   
                        print(f"Game Over! Missed {max_missed_circles} circles. Final Score: {score}")
                        game_over_message()

                # Check for collision with projectiles
                for projectile in projectiles[:]:
                    if detect_collision(circle, projectile):
                        projectiles.remove(projectile)
                        circles.remove(circle)  
                        score += 1 
                        print(f"Score: {score}")
                        break 
                
                # Check for spaceship collision
                if detect_spaceship_collision(circle):
                    print(f"Game Over! Final Score: {score}")
                    game_over_message()

            # Adjust game difficulty based on score
            if score % 5 == 0 and score != 0:
                max_circles += 1
            if score % 5 != 0 and score != 0 and max_circles >2: 
                max_circles -= 1
            if len(circles) < max_circles and random.random() < 0.02:
                circles.append({
                    "x": random.randint(0, WIDTH - circle_radius),
                    "y": 0,
                    "speed": random.uniform(circle_base_speed, circle_base_speed + 1)
                })

        # Draw all game elements
        draw_spaceship(spaceship_x, spaceship_y)
        draw_projectiles()
        draw_circles()
        draw_left_arrow(10, 10, 20, TEAL)
        draw_play_pause(400, 10, 20, AMBER, paused) 
        draw_cross(760, 10, 20, RED)  

        # Display score and missed circles
        font = pygame.font.SysFont(None, 36)
        score_text = font.render(f"Score: {score}", True, WHITE)
        missed_text = font.render(f"Missed: {missed_circles}/{max_missed_circles}", True, WHITE)
        screen.blit(score_text, (10, 50))
        screen.blit(missed_text, (10, 80))

        pygame.display.flip()
        clock.tick(60) 

game_loop()
