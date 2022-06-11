import pygame
from config import *
from player import Player
import math
from map import world_map

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

        pygame.draw.circle(screen, pygame.Color("Green"), player.pos, 12)
        pygame.draw.line(screen, pygame.Color("Green"), player.pos, (player.x + 300 * math.cos(player.angle),
                                                                     player.y + 300 * math.sin(player.angle)))
        for x, y in world_map:
            pygame.draw.rect(screen, pygame.Color("Grey"), (x, y, TILE, TILE), 2)


        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
