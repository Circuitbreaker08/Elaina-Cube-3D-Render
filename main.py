import pygame
import sys

import objects
import math_objects

pygame.init()
info = pygame.display.Info()
screen = pygame.display.set_mode((info.current_w, info.current_h))

class Camera:
    def __init__(self, position: math_objects.Vector3 = math_objects.Vector3(0, 0, 0), rotation: math_objects.Rotation3 = math_objects.Rotation3(0, 0, 0)):
        self.position = position
        self.rotation = rotation

camera = Camera()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

pygame.quit()
sys.exit()