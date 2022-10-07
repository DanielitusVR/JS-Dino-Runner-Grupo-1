import pygame

from dino_runner.components.text_alt import TextAlt

class Score:
    def __init__(self):
        self.score = 0

    def update(self, game):
        self.score += 1
        if self.score % 100 == 0:
            game.game_speed += 2

    def draw(self, screen):
        text = TextAlt(f"Points: {self.score}", 22, 1000, 50,)
        text.draw(screen)

    def restart_score(self):
        self.score = 0
