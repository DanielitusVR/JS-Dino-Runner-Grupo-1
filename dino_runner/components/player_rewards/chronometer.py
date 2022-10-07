from dino_runner.components.player_rewards.reward import Reward
from dino_runner.utils.constants import CHRONOMETER, CHRONOMETER_TYPE


class Chronometer(Reward):
    def __init__(self, position_x, position_y):
        super().__init__(CHRONOMETER, CHRONOMETER_TYPE, position_x, position_y)
