import pygame
from dino_runner.components.player_rewards.half_heart import HalfHeart
from dino_runner.components.player_rewards.chronometer import Chronometer
from dino_runner.components.text_alt import TextAlt
from dino_runner.utils.constants import HALF_HEART


class RewardManager:
    def __init__(self, screen):
        self.start_time_cd = 0
        self.duration = 4
        self.has_reward = False
        self.rewards = []
        self.screen = screen

    def update(self, option):
        x_position = 10
        y_position = 50
        if len(self.rewards) == 0:
            if(option == 0):
                self.rewards.append(HalfHeart(x_position, y_position))
            else:
                self.rewards.append(Chronometer(x_position, y_position))  
            self.has_reward = True
        

    def draw(self, screen):
        reward = self.rewards[0]
        reward.draw(screen)
            