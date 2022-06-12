import pygame
from config import *
from map import world_map


def ray_casting(screen, p_pos, p_angle):
    cur_angle = p_angle - HALF_FOV
    xo, yo = p_pos
    for ray in range(NUM_RAYS):
        sin_a = math.sin(cur_angle)
        cos_a = math.cos(cur_angle)
        for depth in range(MAX_DEPTH):
            x = xo + depth * cos_a
            y = yo + depth * sin_a
            pygame.draw.line(screen, pygame.Color("Green"), p_pos, (x, y), 1)
            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                break
        cur_angle += DELTA_ANGLE
