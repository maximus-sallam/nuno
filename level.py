import pygame 
from settings import *
from tile import Tile
from player import Player
from debug import debug


class Level:
	def __init__(self):

		# get the display surface 
		self.display_surface = pygame.display.get_surface()

		# sprite group setup
		self.visible_sprites = pygame.sprite.Group()
		self.obstacle_sprites = pygame.sprite.Group()

		# sprite setup
		self.create_map()

	def create_map(self):
		for row_index, row in enumerate(WORLD_MAP):
			for col_index, col in enumerate(row):
				x = col_index * TILE_SIZE
				y = row_index * TILE_SIZE
				if col == 'x':
					Tile((x, y), [self.visible_sprites, self.obstacle_sprites])
				if col == 'p':
					self.player = Player((x, y), [self.visible_sprites], self.obstacle_sprites)

	def run(self):
		# update and draw the game
		self.visible_sprites.draw(self.display_surface)
		self.visible_sprites.update()
		debug(self.player.direction)
