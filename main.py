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
        self.angle = 0
        self.flag_x = False

    def update(self, args):
        side = self.side
        if args[pygame.K_UP]:
            if self.side != 'u' and self.side != 'd':
                if side == 'r':
                    self.image = pygame.transform.rotate(self.image, self.angle + 90)
                else:
                    self.image = pygame.transform.rotate(self.image, self.angle - 90)
            elif self.side == 'd':
                self.image = pygame.transform.flip(self.image, False, True)
            self.side = 'u'
            self.rect.y -= 20

        elif args[pygame.K_DOWN]:
            if self.side != 'd' and self.side != 'u':
                if side == 'r':
                    self.image = pygame.transform.rotate(self.image, self.angle - 90)
                else:
                    self.image = pygame.transform.rotate(self.image, self.angle + 90)
            elif self.side == 'u':
                self.image = pygame.transform.flip(self.image, False, True)
            self.side = 'd'
            self.rect.y += 20

        elif args[pygame.K_RIGHT]:
            if self.side != 'r' and self.side != 'l':
                if side == 'u':
                    self.image = pygame.transform.rotate(self.image, self.angle - 90)
                else:
                    self.image = pygame.transform.rotate(self.image, self.angle + 90)
            elif self.side == 'l':
                self.image = pygame.transform.flip(self.image, True, False)
            self.side = 'r'
            self.rect.x += 20

        elif args[pygame.K_LEFT]:
            if self.side != 'l' and self.side != 'r':
                if side == 'u':
                    self.image = pygame.transform.rotate(self.image, self.angle + 90)
                else:
                    self.image = pygame.transform.rotate(self.image, self.angle - 90)
            elif self.side == 'r':
                self.image = pygame.transform.flip(self.image, True, False)
            self.side = 'l'
            self.rect.x -= 20


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