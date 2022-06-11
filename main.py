import pygame
from config import *
from player import Player
import math

pygame.init()
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

        pygame.display.update()
        clock.tick(FPS)


if __name__ == "__main__":
    main()
