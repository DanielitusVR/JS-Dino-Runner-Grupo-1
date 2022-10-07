from pygame.sprite import Sprite


class Reward(Sprite):
    def __init__(self, image, type, x_position, y_position):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = x_position
        self.rect.y = y_position

    def draw(self, screen):
        screen.blit(self.image, self.rect)