# Sprite example
# Introduction to Sprite class

#  Goals
#   * introduce sprite class
#   * subclass the Sprite class (inheritance)

import random
import pygame

# ----- CONSTANTS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
SKY_BLUE = (95, 165, 228)
WIDTH = 1920
HEIGHT = 1080
TITLE = "Sprite Example"
NUM_JEWELS = 75


class Jewel(pygame.sprite.Sprite):
    def __init__(self):
        # call the superclass constructor
        super().__init__()

        # Image is a Surface
        self.image = pygame.Surface((35, 20))
        self.image.fill((100, 255, 100))

        # Rect is a Rectangle (x, y, width, height)
        self.rect = self.image.get_rect()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("./images/link.png")

        self.rect = self.image.get_rect()

    def update(self):
        # changes the position of the player
        # based on the mouse's position
        self.rect.center = pygame.mouse.get_pos()


def main():
    pygame.init()

    # ----- SCREEN PROPERTIES
    size = (WIDTH, HEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption(TITLE)

    # ----- LOCAL VARIABLES
    done = False
    clock = pygame.time.Clock()
    score = 0

    # Sprite group and sprite creation
    all_sprites_group = pygame.sprite.Group()
    jewels_group = pygame.sprite.Group()

    # Jewel creation
    for i in range(NUM_JEWELS):
        jewel = Jewel()
        # Spawn inside the visible screen
        jewel.rect.x = random.randrange(0, WIDTH - jewel.rect.width)
        jewel.rect.y = random.randrange(0, HEIGHT - jewel.rect.height)
        all_sprites_group.add(jewel)
        jewels_group.add(jewel)


    # Player creation
    player = Player()
    all_sprites_group.add(player)

    # ----- MAIN LOOP
    while not done:
        # -- Event Handler
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

        # ----- LOGIC
        all_sprites_group.update()

        # Player collides with jewel
        jewels_collected = pygame.sprite.spritecollide(player, jewels_group, True)
        for jewel in jewels_collected:
            score += 1
            print(score)

        # ----- DRAW
        screen.fill(BLACK)
        all_sprites_group.draw(screen)

        # ----- UPDATE
        pygame.display.flip()
        clock.tick(60)

    pygame.quit()


if __name__ == "__main__":
    main()