import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, pos, groups):
        super().__init__(groups)
        self.image = pygame.image.load('assets/test/player.png').convert_alpha()
        self.rect = self.image.get_rect(topleft=pos)
