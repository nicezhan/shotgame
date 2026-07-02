import pygame
from .constants import PLAYER_WIDTH, PLAYER_HEIGHT, PLAYER_SPEED, PLAYER_HEALTH, PLAYER_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT
from .bullet import Bullet

class Player:
    """
    玩家类，负责玩家角色的移动、射击、碰撞检测和绘制
    
    属性:
        rect: pygame.Rect对象，玩家的矩形区域
        health: 当前生命值
        max_health: 最大生命值
        speed: 移动速度
        bullets: 玩家发射的子弹列表
        last_shoot_time: 上次射击时间
        shoot_cooldown: 射击冷却时间（毫秒）
    """
    
    def __init__(self):
        """初始化玩家，设置初始位置和属性"""
        # 设置玩家初始位置在屏幕底部中央
        self.rect = pygame.Rect(SCREEN_WIDTH // 2 - PLAYER_WIDTH // 2, 
                               SCREEN_HEIGHT - PLAYER_HEIGHT - 20,
                               PLAYER_WIDTH, PLAYER_HEIGHT)
        self.health = PLAYER_HEALTH
        self.max_health = PLAYER_HEALTH
        self.speed = PLAYER_SPEED
        self.bullets = []
        self.last_shoot_time = 0
        self.shoot_cooldown = 200

    def handle_input(self, keys):
        """
        处理玩家输入，控制移动
        
        参数:
            keys: pygame.key.get_pressed()返回的按键状态字典
        """
        # 左移
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.rect.x -= self.speed
        # 右移
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.rect.x += self.speed
        # 上移
        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.rect.y -= self.speed
        # 下移
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.rect.y += self.speed

        # 限制玩家在屏幕范围内移动（下半部分）
        self.rect.x = max(0, min(SCREEN_WIDTH - self.rect.width, self.rect.x))
        self.rect.y = max(SCREEN_HEIGHT // 2, min(SCREEN_HEIGHT - self.rect.height, self.rect.y))

    def shoot(self):
        """发射子弹（带冷却时间限制）"""
        now = pygame.time.get_ticks()
        # 检查是否超过冷却时间
        if now - self.last_shoot_time > self.shoot_cooldown:
            # 创建子弹，从玩家顶部发射，方向向上
            bullet = Bullet(self.rect.centerx, self.rect.top, direction=-1)
            self.bullets.append(bullet)
            self.last_shoot_time = now

    def update(self, enemies):
        """
        更新玩家状态，处理子弹逻辑和碰撞检测
        
        参数:
            enemies: 敌人列表，用于子弹碰撞检测
        """
        # 遍历并更新所有子弹
        for bullet in self.bullets[:]:
            bullet.update()
            
            # 移除超出屏幕的子弹
            if bullet.is_off_screen():
                self.bullets.remove(bullet)
            else:
                # 检测子弹与敌人的碰撞
                for enemy in enemies[:]:
                    if bullet.rect.colliderect(enemy.rect):
                        enemy.take_damage(20)
                        self.bullets.remove(bullet)
                        break

    def draw(self, screen):
        """
        在屏幕上绘制玩家和子弹
        
        参数:
            screen: pygame显示表面
        """
        # 绘制玩家主体
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)
        # 绘制玩家内部高光
        pygame.draw.rect(screen, (100, 150, 200), 
                        (self.rect.x + 5, self.rect.y + 5, 
                         self.rect.width - 10, self.rect.height - 10))
        
        # 绘制所有子弹
        for bullet in self.bullets:
            bullet.draw(screen)

    def take_damage(self, amount):
        """
        玩家受到伤害
        
        参数:
            amount: 伤害值
            
        返回:
            bool: 如果生命值<=0返回True（玩家死亡），否则返回False
        """
        self.health -= amount
        return self.health <= 0