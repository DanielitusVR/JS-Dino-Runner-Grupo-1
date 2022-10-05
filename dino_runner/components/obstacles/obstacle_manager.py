import pygame
import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from .cactus import Cactus


class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def update(self, game):
        option = random.randint(0, 2)

        if(option == 0):
            if len(self.obstacles) == 0:
                self.obstacles.append(Cactus(SMALL_CACTUS))
        elif(option == 1):
            if len(self.obstacles) == 0:
                self.obstacles.append(Cactus(LARGE_CACTUS))
        elif(option == 2):
            if  len(self.obstacles) == 0:
                self.obstacles.append(Bird(BIRD))
        else:
            pass

        for obstacle in self.obstacles:
            obstacle.update(game.game_speed, self.obstacles)
            if game.player.dino_rect.colliderect(obstacle.rect):              
                game.playing = False
                pygame.time.delay(1000)
                break 


    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
