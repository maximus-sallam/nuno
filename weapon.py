import pygame


class Weapon(pygame.sprite.Sprite):
    def __init__(self, player, groups):
        super().__init__(groups)
        direction = player.status.split('_', 1)[0]
        print(direction)

        # graphic
        self.image = pygame.Surface((40, 40))

        # placement
        if direction == 'up':
            self.rect = self.image.get_rect(center=player.rect.center + pygame.math.Vector2(0, -52))
        if direction == 'down':
            self.rect = self.image.get_rect(center=player.rect.center + pygame.math.Vector2(0, 52))
        if direction == 'left':
            self.rect = self.image.get_rect(midright=player.rect.midleft + pygame.math.Vector2(0, 16))
        if direction == 'right':
            self.rect = self.image.get_rect(midleft=player.rect.midright + pygame.math.Vector2(0, 16))
