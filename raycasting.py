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

            if (x // TILE * TILE, y // TILE * TILE) in world_map:
                # depth *= math.cos(player_angle - cur_angle)
                proj_height = PROJ_COEFF / depth
                c = 255 / (1 + depth * depth * 0.00001)
                color = (c, c // 3, c // 4)
                pygame.draw.rect(screen, color, (ray * SCALE, HALF_HEIGHT - proj_height // 2,
                                                 SCALE, proj_height))
                break
        cur_angle += DELTA_ANGLE
