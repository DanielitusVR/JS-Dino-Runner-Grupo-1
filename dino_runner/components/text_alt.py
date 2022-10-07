import pygame

from dino_runner.utils.constants import FONT_STYLE


class TextAlt:
    def __init__(self, text, size, pos_X, pos_Y):
        self.text = text
        self.size = size
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def update(self, text, size, pos_X, pos_Y):
        self.text = text
        self.size = size
        self.pos_X = pos_X
        self.pos_Y = pos_Y

    def change_text(self, text):
        self.text = text

    def set_position(self, pos_x, pos_y):
        self.pos_X += pos_x
        self.pos_Y += pos_y
    
    def set_size(self, size):
        self.size = size

    def draw(self, screen):
        font = pygame.font.Font(FONT_STYLE, self.size)
        text_component = font.render(self.text, True, (0,0,0))
        text_rect = text_component.get_rect()
        text_rect.center = (self.pos_X, self.pos_Y)
        screen.blit(text_component, text_rect)
