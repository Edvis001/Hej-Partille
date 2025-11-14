import time
import sys
import pygame

# testing git hub


class Game:
    def __init__(self):
        pygame.init()

        pygame.display.set_caption("Hej, Partille!")
        self.screen = pygame.display.set_mode((640, 640))

        self.clock = pygame.time.Clock()

# -------------------------------- Load images --------------------------------#
        self.player_moving = pygame.image.load(
            "data/images/characters/char_right.png").convert()
        self.player_moving = pygame.transform.scale(
            self.player_moving, (50, 150))
        self.player_moving.set_colorkey((0, 0, 0))

        self.player_img = pygame.image.load(
            "data/images/characters/char_idle.png").convert()
        self.player_img = pygame.transform.scale(self.player_img, (50, 150))
        self.player_img.set_colorkey((0, 0, 0))

        self.win_screen = pygame.image.load(
            "data/images/background/victory.png").convert()
        self.win_screen = pygame.transform.scale(self.win_screen, (640, 640))

        self.background_1 = pygame.image.load(
            "data/images/background/partille_1.png").convert()
        self.background_1 = pygame.transform.scale(
            self.background_1, (660, 318))
        self.background_1.set_colorkey((0, 0, 0))

        self.sad1 = pygame.image.load(
            "data/images/characters/sad1.png").convert()
        self.sad1 = pygame.transform.scale(self.sad1, (80, 130))
        self.sad1.set_colorkey((0, 0, 0))
        self.sad1_happiness = False

        self.font = pygame.font.Font(None, 14)
        self.tutorial = self.font.render(
            "Tryck E för att säga hej", True, (255, 255, 255))
        self.tutorial = pygame.transform.scale(self.tutorial, (170, 45))

# ------------------------------- Defenitions and cords ----------------------------------------#

        self.player_img_pos = [290, 270]
        self.movement = [False, False]

        self.sad1_collision = pygame.Rect(50, 290, 80, 130)

        self.interact = False

        self.time_passed_since_win = 0

# ---------------------------------------------------------------------------------------------#

    def run(self):
        running = True
        while running:
            # Clear screen
            self.screen.fill((0, 100, 200))

            # Draw background
            self.screen.blit(self.background_1, (-5, 50))

# ------------------------------- Player movement and interactions --------------------------------#

            win = False
            player_hitbox = pygame.Rect(
                self.player_img_pos[0], self.player_img_pos[1], self.player_img.get_width(
                ),
                self.player_img.get_height())
            if player_hitbox.colliderect(self.sad1_collision) and self.interact is True:
                win = True
            elif player_hitbox.colliderect(self.sad1_collision) is True:
                self.screen.blit(self.tutorial, (0, 270))
                self.screen.blit(self.sad1, self.sad1_collision)
            else:
                self.screen.blit(self.sad1, self.sad1_collision)

            self.player_img_pos[0] += (self.movement[1] -
                                       self.movement[0]) * -5
            if not any(self.movement):
                self.screen.blit(self.player_img, self.player_img_pos)
            else:
                if self.movement[0]:
                    self.screen.blit(self.player_moving, self.player_img_pos)
                else:
                    flipped_player_moving = pygame.transform.flip(
                        self.player_moving, True, False)
                    self.screen.blit(flipped_player_moving,
                                     self.player_img_pos)

# ------------------------------- Inputs handling --------------------------------#

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = True
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = True
                    if event.key == pygame.K_e:
                        self.interact = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.movement[0] = False
                    if event.key == pygame.K_LEFT:
                        self.movement[1] = False

            if win is True:
                self.screen.blit(self.win_screen, (0, 0))
                self.movement = [False, False]
                self.time_passed_since_win += self.clock.get_time()
                if self.time_passed_since_win > 3000:
                    running = False

            pygame.display.update()
            self.clock.tick(60)


Game().run()
