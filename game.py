
import pygame as pg
import random
import os
import subprocess



pg.init()
screen = pg.display.set_mode((500, 500))
pg.display.set_caption("Square, Квадрат")

# Creating the player square
square = pg.Surface((55, 55))
square.fill((66, 72, 245))
square_speed = 5
pl_x = 250
pl_y = 400

# Creating the enemy
enemy = pg.Surface((50, 50))
enemy.fill((255, 0, 0))  # RGB for the red color
e_x = random.randint(0, 450)
e_y = 0
enemy_speed_y = 5

# Loading music
pg.mixer.music.load('music/164b99c10472d02.mp3')
pg.mixer.music.play(-1)  # Plays music infinitely

clock = pg.time.Clock()  # To control the frame rate

running = True
while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    keys = pg.key.get_pressed()
    if keys[pg.K_LEFT] and pl_x > 0:
        pl_x -= square_speed
    if keys[pg.K_RIGHT] and pl_x < 445:
        pl_x += square_speed

    # Moving the enemy downward (falling)
    e_y += enemy_speed_y

    # Checking for collision between player and enemy
    if pg.Rect(pl_x, pl_y, 55, 55).colliderect(pg.Rect(e_x, e_y, 50, 50)):
        print("Collision!")# Outputs a message to the console
        enemy.fill((255, 0, 0))  # Changes the enemy's color to green upon collision
        
        # Executing the game_over.py script
        subprocess.run("python game_over.py")
        
        # Relocates the enemy to a random position after a collision
        e_x = random.randint(0, 450)
        e_y = 0

    # If the enemy reaches the bottom of the screen, reset its position to the top
    if e_y > 500:
        e_x = random.randint(0, 450)
        e_y = 0

    screen.fill((0, 0, 0))  # Clears the screen before drawing
    screen.blit(square, (pl_x, pl_y))
    screen.blit(enemy, (e_x, e_y))
    pg.display.update()

    clock.tick(60)  # 60 frames per second

pg.quit()
