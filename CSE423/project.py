import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ring Shot")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
TEAL = (0, 128, 128)
AMBER = (255, 191, 0)

# Game variables
circle_radius = 100
small_circle_radius = 50
gap_angle = 100
rotation_speed = 2  
arrow_speed = 15
balloon_radius = 30
arrow_length = 50  
max_misses = 3
level = 1

# State variables
circle_angle = 0
score = 0
misses = 0
arrow_fired = False
arrow_x, arrow_y = WIDTH // 2, HEIGHT - 50
balloon_visible = True
balloon_x, balloon_y = WIDTH // 2, HEIGHT // 2 - circle_radius - 50
original_balloon_x, original_balloon_y = balloon_x, balloon_y
paused = False

# Clock for controlling frame rate
clock = pygame.time.Clock()


# Midpoint Line Algorithm
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

# Midpoint Circle Algorithm
def draw_circle_midpoint(x_center, y_center, radius, color):
    x = 0
    y = radius
    p = 1 - radius

    def draw_symmetric_points(cx, cy, x, y):
        screen.set_at((cx + x, cy + y), color)
        screen.set_at((cx - x, cy + y), color)
        screen.set_at((cx + x, cy - y), color)
        screen.set_at((cx - x, cy - y), color)
        screen.set_at((cx + y, cy + x), color)
        screen.set_at((cx - y, cy + x), color)
        screen.set_at((cx + y, cy - x), color)
        screen.set_at((cx - y, cy - x), color)

    draw_symmetric_points(x_center, y_center, x, y)

    while x < y:
        x += 1
        if p < 0:
            p += 2 * x + 1
        else:
            y -= 1
            p += 2 * (x - y) + 1
        draw_symmetric_points(x_center, y_center, x, y)

# Reset button using MLA
def draw_left_arrow(x, y, size, color):
    draw_line_midpoint(x + size, y, x, y + size // 2, color)  
    draw_line_midpoint(x, y + size // 2, x + size, y + size, color)  

# play/pause button
def draw_play_pause(x, y, size, color, is_paused):
    if is_paused:
        draw_line_midpoint(x, y, x, y + size, color)
        draw_line_midpoint(x, y, x + size, y + size // 2, color)
        draw_line_midpoint(x + size, y + size // 2, x, y + size, color)
    else:
        draw_line_midpoint(x, y, x, y + size, color)
        draw_line_midpoint(x + size, y, x + size, y + size, color)

# FEXIT button using MLA
def draw_cross(x, y, size, color):
    draw_line_midpoint(x, y, x + size, y + size, color)
    draw_line_midpoint(x + size, y, x, y + size, color)

    
# Rotating circle with two gaps
def draw_rotating_circle(x, y, radius, angle, gap_angle):
    gap1_start = math.radians(angle)
    gap1_end = math.radians(angle + gap_angle)
    gap2_start = math.radians(angle + 180)
    gap2_end = math.radians(angle + 180 + gap_angle)

    pygame.draw.arc(screen, WHITE, (x - radius, y - radius, radius * 2, radius * 2), gap1_end, gap2_start, 5)
    pygame.draw.arc(screen, WHITE, (x - radius, y - radius, radius * 2, radius * 2), gap2_end, gap1_start + 2 * math.pi, 5)
    


# Arrow
def draw_arrow(x, y, angle, arrow_length=50, arrow_width=5, color=(255, 255, 255)):
    # Calculate the end point of the arrow shaft
    end_x = x + arrow_length * math.cos(math.radians(angle))
    end_y = y - arrow_length * math.sin(math.radians(angle))
    
    # Draw the shaft of the arrow using the Midpoint Line Algorithm
    draw_line_midpoint(int(x), int(y), int(end_x), int(end_y), color)

    # Arrowhead (using basic trigonometry to create two lines)
    arrow_angle1 = angle + 135  # One side of the arrowhead
    arrow_angle2 = angle - 135  # Other side of the arrowhead
    
    # Points for the two arrowhead lines
    arrowhead_x1 = end_x + arrow_width * math.cos(math.radians(arrow_angle1))
    arrowhead_y1 = end_y - arrow_width * math.sin(math.radians(arrow_angle1))
    arrowhead_x2 = end_x + arrow_width * math.cos(math.radians(arrow_angle2))
    arrowhead_y2 = end_y - arrow_width * math.sin(math.radians(arrow_angle2))

    # Draw the two lines for the arrowhead using the Midpoint Line Algorithm
    draw_line_midpoint(int(end_x), int(end_y), int(arrowhead_x1), int(arrowhead_y1), color)
    draw_line_midpoint(int(end_x), int(end_y), int(arrowhead_x2), int(arrowhead_y2), color)

# Balloon
def draw_balloon(x, y):
    draw_circle_midpoint(x, y, 50, RED)

# Check collision 
def check_collision():
    global score, arrow_fired, balloon_visible, misses

    if balloon_visible and balloon_y - balloon_radius <= arrow_y <= balloon_y + balloon_radius and balloon_x - balloon_radius <= arrow_x <= balloon_x + balloon_radius:
        arrow_angle = math.degrees(math.atan2(HEIGHT // 2 - arrow_y, arrow_x - WIDTH // 2)) % 360
        gap1_start = circle_angle % 360
        gap1_end = (circle_angle + gap_angle) % 360
        gap2_start = (circle_angle + 180) % 360
        gap2_end = (circle_angle + 180 + gap_angle) % 360

        if ((gap1_start < gap1_end and gap1_start <= arrow_angle <= gap1_end) or
            (gap1_start > gap1_end and (arrow_angle >= gap1_start or arrow_angle <= gap1_end)) or
            (gap2_start < gap2_end and gap2_start <= arrow_angle <= gap2_end) or
            (gap2_start > gap2_end and (arrow_angle >= gap2_start or arrow_angle <= gap2_end))):
            score += 1
            balloon_visible = False
            pygame.time.set_timer(pygame.USEREVENT + 1, 1000)
        else:
            misses += 1

        arrow_fired = False


def reset_balloon():
    global balloon_visible, balloon_x, balloon_y
    balloon_visible = True
    balloon_x = original_balloon_x
    balloon_y = original_balloon_y

def reset_game():
    global score, misses, circle_angle, arrow_fired, balloon_visible
    score = 0
    misses = 0
    circle_angle = 0
    arrow_fired = False
    balloon_visible = True

def reset_miss():
    global misses, circle_angle, arrow_fired, balloon_visible
    misses = 0
    circle_angle = 0
    arrow_fired = False
    balloon_visible = True

def game_over():
    font = pygame.font.SysFont(None, 60)
    text = font.render("Game Over!", True, RED)
    screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()
def game_won():
    font = pygame.font.SysFont(None, 60)
    text = font.render("You Won The Game!", True, RED)
    screen.blit(text, (WIDTH // 2 - 150, HEIGHT // 2 - 30))
    pygame.display.flip()
    pygame.time.delay(3000)
    pygame.quit()
    sys.exit()

# Main game loop
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
                misses = 0
                score = 0
                level = 0
                print("Game Restarted")
            # Play/Pause button
            if 400 <= mouse_x <= 440 and 10 <= mouse_y <= 40:
                paused = not paused
            # Exit button
            if 760 <= mouse_x <= 790 and 10 <= mouse_y <= 40:
                print("Exiting the game.")
                pygame.quit()
                sys.exit()

        if not paused:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and not arrow_fired:
                    arrow_fired = True
                    arrow_x, arrow_y = WIDTH // 2, HEIGHT - 50

            if event.type == pygame.USEREVENT + 1:
                reset_balloon()
                pygame.time.set_timer(pygame.USEREVENT + 1, 0)

    if not paused:
        # Update arrow position
        if arrow_fired:
            arrow_y -= arrow_speed
            if arrow_y < 0:
                arrow_fired = False

        # Update rotating circle angle
        circle_angle = (circle_angle + rotation_speed) % 360

        # Check for collisions
        if arrow_fired:
            check_collision()

        # Level-specific logic
        if score < 4:
            level = 1
            rotation_speed = 1
        elif score < 7:
            level = 2
            rotation_speed = 2
        elif score < 10:
            level = 3
            rotation_speed = 2
        elif score < 16:
            level = 4
            rotation_speed = 3
        elif score < 21:
            level = 5
            rotation_speed = 1
        elif score == 21:
            game_won()

        else:
            game_over()

        if misses >= max_misses:
            game_over()
    

    # Draw rotating circle(s)
    if level == 3 or level == 4:
        draw_rotating_circle(WIDTH // 2, HEIGHT // 2, circle_radius, circle_angle, gap_angle)
        draw_rotating_circle(WIDTH // 2, HEIGHT // 2, small_circle_radius, circle_angle, gap_angle)
    if level == 5:
        draw_rotating_circle(WIDTH // 2, HEIGHT // 2, circle_radius, circle_angle, gap_angle)
        draw_rotating_circle(WIDTH // 2, HEIGHT // 2, small_circle_radius, circle_angle, gap_angle)

        smallest_circle_radius = small_circle_radius // 2 
        draw_rotating_circle(WIDTH // 2, HEIGHT // 2, smallest_circle_radius, circle_angle, gap_angle)
    else:
        draw_rotating_circle(WIDTH // 2, HEIGHT // 2, circle_radius, circle_angle, gap_angle)

    # Draw arrow
    if arrow_fired:
        draw_arrow(arrow_x, arrow_y, -90)

    # Draw balloon
    if balloon_visible:
        draw_balloon(balloon_x, balloon_y)


    font = pygame.font.SysFont(None, 36)
    score_text = font.render(f"Score: {score}", True, WHITE)
    misses_text = font.render(f"Misses: {misses}/{max_misses}", True, WHITE)
    level_text = font.render(f"Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 30))
    screen.blit(misses_text, (10, 60))
    screen.blit(level_text, (10, 90))


    draw_left_arrow(10, 10, 20, TEAL) 
    draw_play_pause(400, 10, 20, AMBER, paused)  
    draw_cross(760, 10, 20, RED)  
    pygame.display.flip()
    clock.tick(60)

pygame.quit()
