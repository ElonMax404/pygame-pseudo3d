import pygame
from config import *
from player import Player
import math
from map import world_map
from raycasting import ray_casting

pygame.init()
pygame.display.set_caption("Pseudo 3d")
screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
player = Player()


def main():
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        player.movement()
        screen.fill(pygame.Color("Black"))

        ray_casting(screen, (player.x, player.y), player.angle)

        pygame.draw.circle(screen, pygame.Color("Green"), (int(player.x), int(player.y)), 12)

        for x, y in world_map:
            pygame.draw.rect(screen, pygame.Color("Grey"), (x, y, TILE, TILE), 2)


        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
