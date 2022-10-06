from dino_runner.components import game
from dino_runner.utils.constants import BIRD
from .obstacle import Obstacle


class Bird(Obstacle):
    POS_BIRD_Y = 265

    def __init__(self, images):
        type = 0
        super().__init__(images, type)
        self.rect.y = self.POS_BIRD_Y
