import math

WIDTH = 1200
HEIGHT = 800
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2

player_pos = (HALF_WIDTH, HALF_HEIGHT)
player_angle = 0
player_speed = 2
FPS = 60
TILE = 100

FOV = math.pi / 3
HALF_FOV = FOV / 2
NUM_RAYS = 120
MAX_DEPTH = 800
DELTA_ANGLE = FOV / NUM_RAYS