import pygame
import os


def load_image(name):
    fullname = os.path.join('data', name)
    image = pygame.image.load(fullname).convert_alpha()
    return image


class MainCharacter(pygame.sprite.Sprite):
    def __init__(self, image, group):
        super().__init__(group)
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.x = 250
        self.rect.y = 250
        self.side = 'r'
        self.angle = 90
        self.flag_x = False

    def update(self, args):
        if args[pygame.K_UP]:
            if self.side != 'u':
                self.image = pygame.transform.flip(self.image, False, True)
                if self.angle != 0:
                    self.image = pygame.transform.rotate()
            self.rect.y -= 20
            self.side = 'u'
        elif args[pygame.K_DOWN]:
            if self.side != 'd':
                self.image = pygame.transform.flip(self.image, False, True)
            self.rect.y += 20
            self.side = 'd'
        elif args[pygame.K_RIGHT]:
            if self.side != 'r':
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x += 20
            self.side = 'r'
        elif args[pygame.K_LEFT]:
            if self.side != 'l':
                self.image = pygame.transform.flip(self.image, True, False)
            self.rect.x -= 20
            self.side = 'l'


pygame.init()
car_sprite = pygame.sprite.Group()
size = width, height = 700, 700
screen = pygame.display.set_mode(size)
screen.fill((255, 255, 255))
main_character = load_image('tank_1.png')
MainCharacter(main_character, car_sprite)
running = True
while running:
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            car_sprite.update(pygame.key.get_pressed())
    car_sprite.draw(screen)
    pygame.display.flip()
pygame.quit()