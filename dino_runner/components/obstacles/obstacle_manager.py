import random
from dino_runner.components.obstacles.bird import Bird
from dino_runner.components.text_alt import TextAlt
from dino_runner.utils.constants import SMALL_CACTUS, LARGE_CACTUS, BIRD
from .cactus import Cactus


class ObstacleManager:


    def __init__(self):
        self.obstacles = []

    def update(self, game_speed, player, on_death):
        if len(self.obstacles) == 0:
            option = random.randint(0, 2)
            if(option == 0):
                 self.obstacles.append(Cactus(SMALL_CACTUS))
            elif(option == 1):
                self.obstacles.append(Cactus(LARGE_CACTUS))
            else:
                self.obstacles.append(Bird(BIRD))

        for obstacle in self.obstacles:
            obstacle.update(game_speed, self.obstacles)
            if player.dino_rect.colliderect(obstacle.rect):            
                if on_death():
                    if(player.has_hammer):
                        player.uses_hammer -= 1
                    self.obstacles.remove(obstacle)
                else:
                    break 
    
    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)

    def reset_obstacles(self):
        self.obstacles = []
