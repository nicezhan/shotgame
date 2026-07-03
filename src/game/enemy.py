import pygame
import random
import os
from .constants import ENEMY_TYPES, SCREEN_WIDTH, SCREEN_HEIGHT, DIFFICULTY_PER_LEVEL
from .bullet import Bullet

class Enemy:
    images_cache = {}
    
    def __init__(self, enemy_type='minion', level_index=0):
        config = ENEMY_TYPES.get(enemy_type, ENEMY_TYPES['minion'])
        self.type = enemy_type
        self.width = config['width']
        self.height = config['height']
        self.speed = config['speed']
        self.health = config['health']
        self.max_health = config['health']
        base_attack = config['attack']
        self.attack = int(base_attack * (1 + level_index * DIFFICULTY_PER_LEVEL))
        self.defense = config['defense']
        self.color = config['color']
        self.score = config['score']
        self.shoot_interval = config['shoot_interval']
        
        self.rect = pygame.Rect(random.randint(50, SCREEN_WIDTH - self.width - 50),
                               -self.height,
                               self.width, self.height)
        
        self.move_direction = random.choice([-1, 1])
        self.last_shoot_time = 0
        self.bullets = []
        self.move_timer = 0
        self.change_direction_interval = random.randint(1000, 3000)
        
        self.image = self._load_image(enemy_type)

    @classmethod
    def _load_image(cls, enemy_type):
        if enemy_type in cls.images_cache:
            return cls.images_cache[enemy_type]
        
        images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "images")
        images_dir = os.path.normpath(images_dir)
        filename = f"enemy_{enemy_type}.png"
        
        try:
            img = pygame.image.load(os.path.join(images_dir, filename)).convert_alpha()
            config = ENEMY_TYPES.get(enemy_type, ENEMY_TYPES['minion'])
            scaled_img = pygame.transform.scale(img, (config['width'], config['height']))
            cls.images_cache[enemy_type] = scaled_img
            return scaled_img
        except Exception as e:
            return None

    def update(self, player):
        self.rect.y += self.speed
        
        self.move_timer += 16
        if self.move_timer > self.change_direction_interval:
            self.move_direction *= -1
            self.move_timer = 0
            self.change_direction_interval = random.randint(1000, 3000)
        
        self.rect.x += self.move_direction * self.speed * 0.5
        
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.move_direction *= -1
        
        self.shoot(player)
        
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

    def shoot(self, player):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > self.shoot_interval:
            bullet = Bullet(self.rect.centerx, self.rect.bottom, direction=1, damage=self.attack)
            self.bullets.append(bullet)
            self.last_shoot_time = now

    def take_damage(self, amount):
        actual_damage = max(1, amount - self.defense)
        self.health -= actual_damage
        return self.health <= 0

    def is_off_screen(self):
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        if self.image:
            screen.blit(self.image, self.rect)
        else:
            pygame.draw.rect(screen, self.color, self.rect)
        
        health_ratio = self.health / self.max_health
        health_bar_width = self.rect.width * health_ratio
        pygame.draw.rect(screen, (255, 0, 0), 
                        (self.rect.x, self.rect.y - 5, 
                         self.rect.width, 3))
        pygame.draw.rect(screen, (0, 255, 0), 
                        (self.rect.x, self.rect.y - 5, 
                         health_bar_width, 3))
        
        for bullet in self.bullets:
            bullet.draw(screen)