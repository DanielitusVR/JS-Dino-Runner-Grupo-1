import pygame

from dino_runner.utils.constants import FONT_STYLE


class TextAlt:
    def __init__(self, text, size, pos_X, pos_Y, screen):
        self.text = text
        self.size = size
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.screen = screen

    def update(self, text, size, pos_X, pos_Y):
        self.text = text
        self.size = size
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def draw(self):
        font = pygame.font.Font(FONT_STYLE, self.size)
        text_component = font.render(self.text, True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (self.pos_X, self.pos_Y)
        self.screen.blit(text_component, text_rect)
