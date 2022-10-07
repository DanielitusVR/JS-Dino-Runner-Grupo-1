from dino_runner.components.player_rewards.reward import Reward
from dino_runner.utils.constants import HALF_HEART, HALF_HEART_TYPE


class HalfHeart(Reward):
    def __init__(self, position_x, position_y):
        super().__init__(HALF_HEART, HALF_HEART_TYPE, position_x, position_y)