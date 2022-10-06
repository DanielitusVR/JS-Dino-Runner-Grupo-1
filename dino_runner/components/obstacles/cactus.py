import random

from dino_runner.utils.constants import LARGE_CACTUS, SMALL_CACTUS
from .obstacle import Obstacle

class Cactus(Obstacle):
    SMALL_CACTUS_Y = 325
    LARGE_CACTUS_Y = 300
    
    def __init__(self, images):
        type = random.randint(0,2)
        super().__init__(images, type)

        if images == LARGE_CACTUS:
            self.rect.y = self.LARGE_CACTUS_Y
        elif images == SMALL_CACTUS:
            self.rect.y = self.SMALL_CACTUS_Y