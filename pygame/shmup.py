# shmup.py
# Top-down shoot-em-up game
# Goals"
#   - get more comfortable with sprites and mouse movement
#   - create new sprites IN the main loop (bullets)
#   - using pygame.mouse a little more comfortably

import pygame
import random

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 720
HEIGHT = 1000
TITLE = "<SHMUP"
NUM_ROWS = 8

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/galaga_ship.png")
        # scaling the image down 0.5x
        self.image = pygame.transform.scale(self.image, (64,64))

        self.rect = self.image.get_rect()

    def update(self):
        # move player with mouse
        self.rect.center = pygame.mouse.get_pos()

        if self.rect.top < HEIGHT - 100:
            self.rect.top = HEIGHT - 100

class Enemy(pygame.sprite.Sprite):
    def __init__(self, y_coord):
        # y_coord = initial y-coordinate

        super().__init__()

        self.image = pygame.image.load("./images/mario.png")

        self.rect = self.image.get_rect()
        # Initial location middle of screen
        self.rect.centerx = WIDTH/2
        self.rect.centery = y_coord

        self.x_vel = 3

    def update(self):
        # Move the enemy side-to-side
        self.rect.x += self.x_vel

        # Keep the enemy in the screen
        if self.rect.right > WIDTH or self.rect.left < 0:
            self.x_vel *= -1

class Bullet(pygame.sprite.Sprite):
    def __init__(self, coords):
        # Arguments: coords - tuple of x,y
        super().__init__()

        self.image = pygame.image.load("./images/bullet.png")
        # scale to 22x36px
        self.image = pygame.transform.scale(self.image, (22,36))
        # create hitbox after scaling image to avoid confusion
        self.rect = self.image.get_rect()
        # start bullet at coords
        self.rect.centerx, self.rect.bottom = coords

        self.y_vel = -3

    def update(self):
        self.rect.y += self.y_vel


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()

    # Sprite Groups
    all_sprites = pygame.sprite.RenderUpdates()
    enemy_sprites = pygame.sprite.Group()
    player_bullet_sprites = pygame.sprite.Group()

    # --- enemies
    for i in range(NUM_ROWS):
        enemy = Enemy(100 + i*40)
        enemy.rect.x = enemy.rect.x - random.choice([-10, 10])
        all_sprites.add(enemy)
        enemy_sprites.add(enemy)

    # --- player
    player = Player()
    all_sprites.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if len(player_bullet_sprites) < 3:
                    # create a bullet
                    bullet = Bullet(player.rect.midtop)
                    all_sprites.add(bullet)
                    player_bullet_sprites.add(bullet)

        # ----- LOGIC
        all_sprites.update()

        # check if every bullet has collided with enemy
        for bullet in player_bullet_sprites:
            # kill bullet if off-screen
            if bullet.rect.bottom < 0:
                bullet.kill()

            # enemy collide = group, what it collides with, kill it?
            enemy_hit_group = pygame.sprite.spritecollide(bullet, enemy_sprites, True)
            if len(enemy_hit_group) > 0:
                bullet.kill()



        # ----- DRAW
        screen.fill(BLACK)
        # draw and return just dirty rectangles
        dirty_rectangles = all_sprites.draw(screen)

        # ----- UPDATE
        # update dirty rectangles
        pygame.display.update(dirty_rectangles)
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()