import pygame
import os
from .constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_HEALTH, SCREEN_WIDTH, SCREEN_HEIGHT
from .bullet import Bullet

class Player:
    def __init__(self):
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, 
                               SCREEN_HEIGHT - PLAYER_HEIGHT - 20,
                               PLAYER_WIDTH, PLAYER_HEIGHT)
        self.health = PLAYER_HEALTH
        self.max_health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.bullets = []
        self.last_shoot_time = 0
        self.shoot_cooldown = 200
        
        self.images = self._load_images()
        self.current_frame = 0
        self.animation_timer = 0
        self.is_moving = False
        self.is_shooting = False
        self.shoot_animation_time = 0

    def _load_images(self):
        images_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "assets", "images")
        images_dir = os.path.normpath(images_dir)
        images = {}
        
        try:
            idle_img = pygame.image.load(os.path.join(images_dir, "player_idle.png")).convert_alpha()
            images['idle'] = pygame.transform.scale(idle_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            
            run1_img = pygame.image.load(os.path.join(images_dir, "player_run_1.png")).convert_alpha()
            images['run_1'] = pygame.transform.scale(run1_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            
            run2_img = pygame.image.load(os.path.join(images_dir, "player_run_2.png")).convert_alpha()
            images['run_2'] = pygame.transform.scale(run2_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
            
            shoot_img = pygame.image.load(os.path.join(images_dir, "player_shoot.png")).convert_alpha()
            images['shoot'] = pygame.transform.scale(shoot_img, (PLAYER_WIDTH, PLAYER_HEIGHT))
        except Exception as e:
            images = None
        
        return images

    def handle_input(self, keys):
        self.is_moving = False
        
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
            self.is_moving = True
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
            self.is_moving = True
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
            self.is_moving = True
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed
            self.is_moving = True

        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(SCREEN_HEIGHT // 2, min(SCREEN_HEIGHT - self.rect.height, self.rect.y))

    def shoot(self):
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > self.shoot_cooldown:
            bullet = Bullet(self.rect.centerx, self.rect.top, direction=-1, damage=20)
            self.bullets.append(bullet)
            self.last_shoot_time = now
            self.is_shooting = True
            self.shoot_animation_time = 100

    def update(self, enemies):
        now = pygame.time.get_ticks()
        
        if self.is_shooting:
            self.shoot_animation_time -= 16
            if self.shoot_animation_time <= 0:
                self.is_shooting = False
        
        self.animation_timer += 16
        if self.animation_timer > 100:
            self.animation_timer = 0
            if self.is_moving:
                self.current_frame = (self.current_frame + 1) % 2
        
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
            else:
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.take_damage(20)
                        self.bullets.remove(bullet)
                        break

    def draw(self, screen):
        if self.images:
            if self.is_shooting:
                screen.blit(self.images['shoot'], self.rect)
            elif self.is_moving:
                frame_key = 'run_1' if self.current_frame == 0 else 'run_2'
                screen.blit(self.images[frame_key], self.rect)
            else:
                screen.blit(self.images['idle'], self.rect)
        else:
            pygame.draw.rect(screen, (70, 130, 180), self.rect)
        
        for bullet in self.bullets:
            bullet.draw(screen)

    def take_damage(self, amount):
        self.health -= amount
        return self.health <= 0