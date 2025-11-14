import time
import sys
import pygame


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

        self.partille_l1_1 = pygame.image.load(
            "data/images/background/partille_1.png").convert()
        self.partille_l1_1 = pygame.transform.scale(
            self.partille_l1_1, (660, 318))
        self.partille_l1_1.set_colorkey((0, 0, 0))

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

        self.layer1_pos = [0, 150]
        self.layer1_movement = [False, False]

        self.sad1_collision = None

        # Define states
        self.interact = False
        self.running = True
        self.win = False

        self.time_passed_since_win = 0

# ---------------------------------------------------------------------------------------------#

    def run(self):

        while self.running:
            # Clear screen
            self.screen.fill((0, 100, 200))

# ------------------------------- Draw layers --------------------------------#

            self.screen.blit(self.partille_l1_1, self.layer1_pos)


# ------------------------------- Hitboxes --------------------------------#

            player_hitbox = pygame.Rect(
                320, 380, self.player_img.get_width(
                ),
                self.player_img.get_height())

            self.sad1_collision = pygame.Rect(
                self.layer1_pos[0] + 50, self.layer1_pos[1] + 250, 80, 130)
            # Show hitboxes for testing
            pygame.draw.rect(self.screen, (255, 0, 0), player_hitbox, 2)
            pygame.draw.rect(self.screen, (0, 255, 0), self.sad1_collision, 2)

# ------------------------------- Player movement and interactions --------------------------------#

            if player_hitbox.colliderect(self.sad1_collision) and self.interact is True:
                self.win = True
            elif player_hitbox.colliderect(self.sad1_collision) is True:
                self.screen.blit(self.tutorial, (0, 270))
                self.screen.blit(self.sad1, self.sad1_collision)
            else:
                self.screen.blit(self.sad1, self.sad1_collision)

            self.layer1_pos[0] += (self.layer1_movement[1] -
                                   self.layer1_movement[0]) * 5
            if not any(self.layer1_movement):
                self.screen.blit(
                    self.player_img, player_hitbox.topleft)
            else:
                if self.layer1_movement[0]:
                    self.screen.blit(self.player_moving, player_hitbox.topleft)
                else:
                    flipped_player_moving = pygame.transform.flip(
                        self.player_moving, True, False)
                    self.screen.blit(flipped_player_moving,
                                     (player_hitbox.topleft))

# ------------------------------- Inputs handling --------------------------------#

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        self.layer1_movement[0] = True
                    if event.key == pygame.K_LEFT:
                        self.layer1_movement[1] = True
                    if event.key == pygame.K_e:
                        self.interact = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_RIGHT:
                        self.layer1_movement[0] = False
                    if event.key == pygame.K_LEFT:
                        self.layer1_movement[1] = False

# ------------------------------- Win condition --------------------------------#

            if self.win is True:
                self.screen.blit(self.win_screen, (0, 0))
                self.layer1_movement = [False, False]
                self.time_passed_since_win += self.clock.get_time()
                if self.time_passed_since_win > 3000:
                    self.running = False

# ---------------------------------------------------------------------------------------------#

            pygame.display.update()
            self.clock.tick(60)


Game().run()
