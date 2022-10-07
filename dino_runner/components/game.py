import pygame
from dino_runner.components.dinosaur import Dinosaur
from dino_runner.components.obstacles.obstacle_manager import ObstacleManager
from dino_runner.components.player_hearts.player_heart_manager import PlayerHeartManager
from dino_runner.components.powerups.power_up_manager import PowerUpManager
from dino_runner.components.score import Score
from dino_runner.components.text_alt import TextAlt

from dino_runner.utils.constants import BG, DEFAULT_TYPE, ICON, SCREEN_HEIGHT, SCREEN_WIDTH, SHIELD_TYPE, TITLE, FPS, RUNNING, DEATH

class Game:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption(TITLE)
        pygame.display.set_icon(ICON)
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        self.clock = pygame.time.Clock()
        self.playing = False
        self.executing = False
        self.game_speed = 20
        self.x_pos_bg = 0
        self.y_pos_bg = 380

        self.player = Dinosaur()
        self.obstacle_manager = ObstacleManager()
        self.power_up_manager = PowerUpManager()
        self.heart_manager = PlayerHeartManager()

        self.death_count = 0
        self.score = Score() 

    def execute(self):
        self.executing = True
        self.obstacle_manager.reset_obstacles()
        while self.executing:
            if not self.playing:
                self.show_menu()

        pygame.quit()

    def run(self):
        # Game loop: events - update - draw
        self.playing = True
        self.reset_game()
        while self.playing:
            self.events()
            self.update()
            self.draw()


    def reset_game(self):
        self.game_speed = 20
        self.obstacle_manager.reset_obstacles()
        self.score.restart_score()
        self.power_up_manager.reset_power_ups()
        self.heart_manager.reset_hearts()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False

    def update(self):
        user_input = pygame.key.get_pressed()
        self.player.update(user_input)
        self.obstacle_manager.update(self.game_speed, self.player, self.on_death)
        self.score.update(self)
        self.power_up_manager.update(self.game_speed, self.player, self.score.score)

    def draw(self):
        self.clock.tick(FPS)
        self.screen.fill((255, 255, 255))
        self.draw_background()
        self.player.draw(self.screen)
        self.obstacle_manager.draw(self.screen)
        self.score.draw(self.screen)
        self.power_up_manager.draw(self.screen)
        self.heart_manager.draw(self.screen)
        self.draw_power_up_active()
        pygame.display.update()
        pygame.display.flip()

    def draw_background(self):
        image_width = BG.get_width()
        self.screen.blit(BG, (self.x_pos_bg, self.y_pos_bg))
        self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
        if self.x_pos_bg <= -image_width:
            self.screen.blit(BG, (image_width + self.x_pos_bg, self.y_pos_bg))
            self.x_pos_bg = 0
        self.x_pos_bg -= self.game_speed

    def show_menu(self): 
        self.screen.fill((255, 255, 255))
        half_screen_height = SCREEN_HEIGHT // 2
        half_screen_width = SCREEN_WIDTH // 2

        if self.death_count == 0:
            text = TextAlt("Press any key to start", 30, half_screen_width, half_screen_height, self.screen)
            text.draw()
            dino_image = RUNNING[0]
        else:
            text = TextAlt("YOU DIED. Press any key to retry", 30, half_screen_width, half_screen_height, self.screen)
            text.draw()
            
            text.update(f"Count of Deaths: {self.death_count}", 25, half_screen_width, half_screen_height + 40)
            text.draw()

            text.update(f"Points: {self.score.score}", 25, half_screen_width, half_screen_height + 75)
            text.draw()

            dino_image = DEATH

        self.screen.blit(dino_image, (half_screen_width - 35, half_screen_height - 140))
        pygame.display.update()
        self.handle_key_events_on_menu()

    def handle_key_events_on_menu(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.executing = False
            elif event.type == pygame.KEYDOWN:
                self.run()

    def on_death(self):
        is_invincible = self.player.type == SHIELD_TYPE and self.heart_manager.heart_count > 0
        self.heart_manager.reduce_heart
        if not is_invincible:
            pygame.time.delay(500)
            self.playing = False
            self.death_count += 1
            
        return is_invincible

    def draw_power_up_active(self):
        if self.player.has_power_up:
            time_to_show = round((self.player.power_up_time_up - pygame.time.get_ticks()) / 1000, 2)
            if time_to_show >= 0:
                text = TextAlt(f"{self.player.type.capitalize()} enable for {time_to_show} seconds.", 18, 600, 40, self.screen)
                text.draw()
            else:
                self.player.has_power_up = False
                self.player.type = DEFAULT_TYPE
