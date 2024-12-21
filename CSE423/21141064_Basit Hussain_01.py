# from OpenGL.GL import * 
# from OpenGL.GLUT import *
# from OpenGL.GLU import *
# import random

# # Variables for use later
# rain_dir = 0  # 0: Straight, -1: Left, 1: Right
# backg_col = [0.0, 0.0, 0.0]
# rain_dro = []
# WindSize = 500

# # raindrop initialization
# for _ in range(100):
#     rain_dro.append([random.randint(0, WindSize), random.randint(0, WindSize)])

# def draw_house():
#     # Draw house body
#     glColor3f(0.6, 0.3, 0.0)  
#     glBegin(GL_QUADS)
#     glVertex2f(100, 0)   # Bottom-left corner (house body)
#     glVertex2f(400, 0)   # Bottom-right corner
#     glVertex2f(400, 200) # Top-right corner
#     glVertex2f(100, 200) # Top-left corner
#     glEnd()
    
#     # Draw roof
#     glColor3f(0.8, 0.4, 0.4)  
#     glBegin(GL_TRIANGLES)
#     glVertex2f(80, 200)   # Left corner of the roof
#     glVertex2f(420, 200)  # Right corner of the roof
#     glVertex2f(250, 300)  # Top of the roof
#     glEnd()

#     # Draw door
#     glColor3f(0.4, 0.2, 0.0)  
#     glBegin(GL_QUADS)
#     glVertex2f(220, 0)   # Bottom-left corner of the door
#     glVertex2f(280, 0)   # Bottom-right corner of the door
#     glVertex2f(280, 120) # Top-right corner of the door
#     glVertex2f(220, 120) # Top-left corner of the door
#     glEnd()

#     # Draw left window
#     glColor3f(0.7, 0.9, 1.0)  
#     glBegin(GL_QUADS)
#     glVertex2f(130, 130)  # Bottom-left corner of the left window
#     glVertex2f(180, 130)  # Bottom-right corner
#     glVertex2f(180, 170)  # Top-right corner
#     glVertex2f(130, 170)  # Top-left corner
#     glEnd()

#     # Draw right window
#     glColor3f(0.7, 0.9, 1.0)  
#     glBegin(GL_QUADS)
#     glVertex2f(320, 130)  # Bottom-left corner of the right window
#     glVertex2f(370, 130)  # Bottom-right corner
#     glVertex2f(370, 170)  # Top-right corner
#     glVertex2f(320, 170)  # Top-left corner
#     glEnd()

#     # Draw chimney
#     glColor3f(0.5, 0.1, 0.1)  
#     glBegin(GL_QUADS)
#     glVertex2f(320, 230)  # Bottom-left corner of the chimney
#     glVertex2f(360, 230)  # Bottom-right corner
#     glVertex2f(360, 280)  # Top-right corner
#     glVertex2f(320, 280)  # Top-left corner
#     glEnd()

# def draw_rain():
#     global rain_dro, rain_dir
#     glColor3f(0.5, 0.5, 1.0)  
#     glPointSize(2)
#     glBegin(GL_POINTS)
#     for drop in rain_dro:
#         glVertex2f(drop[0], drop[1])
#         # Update rain position
#         drop[1] -= 5  # Falling speed
#         drop[0] += rain_dir  # Directional movement
#         if drop[1] < 0:  # Reset when it falls below the screen
#             drop[1] = WindSize
#             drop[0] = random.randint(0, WindSize)
#     glEnd()

# def change_background(lighten=True):
#     global backg_col
#     step = 0.05
#     if lighten:
#         backg_col = [min(1.0, c + step) for c in backg_col]
#     else:
#         backg_col = [max(0.0, c - step) for c in backg_col]
#     glClearColor(*backg_col, 1.0)

# def keyboard(key, x, y):
#     global rain_dir
#     if key == b'd':  # Gradually lighten the background (daytime)
#         change_background(lighten=True)
#     elif key == b'n':  # Gradually darken the background (nighttime)
#         change_background(lighten=False)

# def special_input(key, x, y):
#     global rain_dir
#     if key == GLUT_KEY_LEFT:  # Bend rain to the left
#         rain_dir = max(rain_dir - 1, -5)
#     elif key == GLUT_KEY_RIGHT:  # Bend rain to the right
#         rain_dir = min(rain_dir + 1, 5)

# def iterate():
#     glViewport(0, 0, WindSize, WindSize)
#     glMatrixMode(GL_PROJECTION)
#     glLoadIdentity()
#     glOrtho(0.0, WindSize, 0.0, WindSize, 0.0, 1.0)
#     glMatrixMode(GL_MODELVIEW)
#     glLoadIdentity()

# def show_screen():
#     glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
#     glLoadIdentity()
#     iterate()
#     draw_house()
#     draw_rain()
#     glutSwapBuffers()

# # Timer for animation
# def timer(value):
#     glutPostRedisplay()
#     glutTimerFunc(16, timer, 0)

# # Main Function
# glutInit()
# glutInitDisplayMode(GLUT_RGBA)
# glutInitWindowSize(WindSize, WindSize)
# glutInitWindowPosition(0, 0)
# wind = glutCreateWindow(b"21141064_Basit Hussain_01")
# glutDisplayFunc(show_screen)
# glutTimerFunc(0, timer, 0)
# glutKeyboardFunc(keyboard)
# glutSpecialFunc(special_input)
# glClearColor(*backg_col, 1.0)
# glutMainLoop()



from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
import random
import time

# Global variables
points = []
directions = []
speeds = 1.0
frozen = False
blinking = False
colors = []
last_blink_time = time.time()

# generate random colors
def random_color():
    return random.random(), random.random(), random.random()

# Update positions of points
def update_points():
    global points, directions, frozen
    if frozen:
        return
    for i in range(len(points)):
        x, y = points[i]
        dx, dy = directions[i]
        
        # Update position
        x += dx * speeds
        y += dy * speeds
        if x <= 0 or x >= 500:
            dx *= -1
        if y <= 0 or y >= 500:
            dy *= -1

        directions[i] = (dx, dy)
        points[i] = (x, y)

def draw_points():
    global points, colors, blinking, last_blink_time
    current_time = time.time()
    for i in range(len(points)):
        x, y = points[i]
        if blinking and int((current_time - last_blink_time) * 2) % 2 == 1:
            glColor3f(0, 0, 0)
        else:
            glColor3f(*colors[i])
        glPointSize(5)
        glBegin(GL_POINTS)
        glVertex2f(x, y)
        glEnd()

# Handle mouse input
def mouse_click(button, state, x, y):
    global points, directions, colors, blinking
    if state == GLUT_DOWN:
        if button == GLUT_RIGHT_BUTTON and not frozen:
            x = x
            y = 500 - y
            dx = random.choice([-1, 1])
            dy = random.choice([-1, 1])
            points.append((x, y))
            directions.append((dx, dy))
            colors.append(random_color())
        elif button == GLUT_LEFT_BUTTON and not frozen:
            blinking = not blinking

def keyboard_input(key, x, y):
    global speeds, frozen
    if key == b'\x20': 
        frozen = not frozen  
    elif not frozen:
        if key == GLUT_KEY_UP:
            speeds += 0.5
        elif key == GLUT_KEY_DOWN:
            speeds = max(0.5, speeds - 0.5)


def showScreen():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()
    iterate()
    update_points()
    draw_points()
    glutSwapBuffers()


def iterate():
    glViewport(0, 0, 500, 500)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glOrtho(0.0, 500, 0.0, 500, 0.0, 1.0)
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()


def timer(value):
    glutPostRedisplay()
    glutTimerFunc(16, timer, 0)  


glutInit()
glutInitDisplayMode(GLUT_RGBA)
glutInitWindowSize(500, 500)
glutInitWindowPosition(0, 0)
wind = glutCreateWindow(b"OpenGL Amazing Box")


glutDisplayFunc(showScreen)
glutMouseFunc(mouse_click)
glutSpecialFunc(keyboard_input)
glutTimerFunc(16, timer, 0)
glutMainLoop()

