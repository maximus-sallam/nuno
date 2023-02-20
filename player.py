import pygame
from support import import_folder

class Player(pygame.sprite.Sprite):
	def __init__(self, pos, groups, obstacle_sprites):
		super().__init__(groups)
		self.image = pygame.image.load('assets/test/player.png').convert_alpha()
		self.rect = self.image.get_rect(topleft=pos)
		self.hitbox = self.rect.inflate(0, -26)

		# graphics setup
		self.import_player_assets()
		self.status = 'down'

		# movement
		self.direction = pygame.math.Vector2()
		self.speed = 5

		# attack timer
		self.attacking = False
		self.attack_cooldown = 400
		self.attack_time = None

		self.obstacle_sprites = obstacle_sprites

	def import_player_assets(self):
		character_patch = 'assets/images/player/'
		self.animations = {
			'up': [], 'down': [], 'left': [], 'right': [],
			'up_idle': [], 'down_idle': [], 'left_idle': [], 'right_idle': [],
			'up_attack': [], 'down_attack': [], 'left_attack': [], 'right_attack': []
		}

		for animation in self.animations.keys():
			full_path = character_patch + animation
			self.animations[animation] = import_folder(full_path)

	def input(self):
		keys = pygame.key.get_pressed()

		# movement input
		if keys[pygame.K_UP]:
			self.direction.y = -1
			self.status = 'up'
		elif keys[pygame.K_DOWN]:
			self.direction.y = 1
			self.status = 'down'
		else:
			self.direction.y = 0

		if keys[pygame.K_RIGHT]:
			self.direction.x = 1
			self.status = 'right'
		elif keys[pygame.K_LEFT]:
			self.direction.x = -1
			self.status = 'left'
		else:
			self.direction.x = 0

		# attack input
		if keys[pygame.K_SPACE] and not self.attacking:
			self.attacking = True
			self.attack_time = pygame.time.get_ticks()
			print('Attack!')

		# magic input
		if keys[pygame.K_LCTRL] and not self.attacking:
			self.attacking = True
			self.attack_time = pygame.time.get_ticks()
			print('Magic!')

	def get_status(self):

		# idle status
		if self.direction.x == 0 and self.direction.y == 0:
			if 'idle' not in self.status and 'attack' not in self.status:
				self.status = self.status + '_idle'

		if self.attacking:
			self.direction.x = 0
			self.direction.y = 0
			if 'attack' not in self.status:
				if 'idle' in self.status:
					# overwrite idle
					self.status = self.status.replace('_idle', '_attack')
				else:
					self.status = self.status + '_attack'
		else:
			if 'attack' in self.status:
				self.status = self.status.replace('_attack', '_idle')

	def move(self, speed):
		if self.direction.magnitude() != 0:
			self.direction = self.direction.normalize()

		self.hitbox.x += self.direction.x * speed
		self.collision('horizontal')
		self.hitbox.y += self.direction.y * speed
		self.collision('vertical')
		self.rect.center = self.hitbox.center

	def collision(self, direction):
		if direction == 'horizontal':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.x > 0:  # moving right
						self.hitbox.right = sprite.hitbox.left
					if self.direction.x < 0:  # moving left
						self.hitbox.left = sprite.hitbox.right

		if direction == 'vertical':
			for sprite in self.obstacle_sprites:
				if sprite.hitbox.colliderect(self.hitbox):
					if self.direction.y > 0:  # moving down
						self.hitbox.bottom = sprite.hitbox.top
					if self.direction.y < 0:  # moving up
						self.hitbox.top = sprite.hitbox.bottom

	def cooldowns(self):
		current_time = pygame.time.get_ticks()

		if self.attacking:
			if current_time - self.attack_time >= self.attack_cooldown:
				self.attacking = False

	def update(self):
		self.input()
		self.cooldowns()
		self.get_status()
		self.move(self.speed)
