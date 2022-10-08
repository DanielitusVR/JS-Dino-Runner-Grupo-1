from random import randint
from secrets import randbelow
import pygame
from dino_runner.components.obstacles import obstacle_manager
from dino_runner.components.player_rewards.half_heart import HalfHeart
from dino_runner.components.player_rewards.chronometer import Chronometer
from dino_runner.components.text_alt import TextAlt
from dino_runner.utils.constants import CHRONOMETER, CHRONOMETER_TYPE, HALF_HEART


class RewardManager:
    def __init__(self):
        self.start_time_cd = 0
        self.duration = 4
        self.rewards = []

    def generate_reward(self):
        option = randint(0,1)
        if len(self.rewards == 0):
            if(option == 0):
                self.rewards.append(HalfHeart())
            else:
                self.rewards.append(Chronometer())

    def update(self, player, obstacle_manager):
        if(player.dino_rect.colliderect(obstacle_manager.obstacles[0].rect)):
            for reward in self.rewards:
                reward.start_time = pygame.time.get_ticks()
                player.reward_cooldown(reward.start_time, reward.duration_cd)
                self.power_ups.remove(reward)

    def draw(self, screen):
        reward = self.rewards[0]
        reward.draw(screen)

    def reset_rewards(self):
        self.rewards = []
