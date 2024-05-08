import math
import random
import time
import pygame

class LidarDummy:

    def __init__(self):
        pass

    def __next__(self):
        dummy = {}
        for x in range(360):
            dummy[x] = random.randint(60, 80)
        return dummy




def draw_values(screen, values):
    points = []
    sx, sy = screen.get_size()
    for angle, distance in values.items():
        winkel = math.radians(angle)
        if values[angle] is not None:
            x = math.cos(winkel) * distance
            y = math.sin(winkel) * distance
            points.append((x/10 + sx/2, y/10 + sy/2))
    screen.fill((0, 0, 0))
    for point in points:
        pygame.draw.circle(screen, (255, 255, 255), point, 5)
    pygame.display.flip()



def main(lidar):
    running = True
    pygame.init()
    pygame.display.set_caption("Chenzen Lidar")
    screen = pygame.display.set_mode((700, 700))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        werte = lidar #Felix :werte = next(lidar)
        draw_values(screen, werte)
        time.sleep(1)
