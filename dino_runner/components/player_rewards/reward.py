from pygame.sprite import Sprite


class Reward(Sprite):
    def __init__(self, image, type):
        self.image = image
        self.type = type
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 0
        self.reward_cd = 5

    def set_position(self, pos_x, pos_y):
        self.rect.x = pos_x
        self.rect.y = pos_y
    
    def draw(self, screen):
        screen.blit(self.image, (self.rect.x, self.rect.y))