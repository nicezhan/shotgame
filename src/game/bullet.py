import pygame
from .constants import BULLET_WIDTH, BULLET_HEIGHT, BULLET_SPEED, BULLET_COLOR, PLAYER_BULLET_COLOR, SCREEN_WIDTH, SCREEN_HEIGHT

class Bullet:
    """
    子弹类，负责子弹的移动、碰撞检测和绘制
    
    属性:
        rect: pygame.Rect对象，子弹的矩形区域
        speed: 子弹速度（正数向下，负数向上）
        direction: 子弹方向（1向下，-1向上）
        color: 子弹颜色
        damage: 子弹伤害值
    """
    
    def __init__(self, x, y, direction=1, damage=10):
        """
        初始化子弹
        
        参数:
            x: 子弹初始x坐标
            y: 子弹初始y坐标
            direction: 子弹方向，1表示向下（敌人子弹），-1表示向上（玩家子弹）
            damage: 子弹伤害值，默认为10
        """
        self.rect = pygame.Rect(x - BULLET_WIDTH // 2, y, BULLET_WIDTH, BULLET_HEIGHT)
        self.speed = BULLET_SPEED * direction
        self.direction = direction
        self.damage = damage
        # 根据方向设置颜色
        self.color = PLAYER_BULLET_COLOR if direction == -1 else BULLET_COLOR

    def update(self):
        """更新子弹位置"""
        self.rect.y += self.speed

    def is_off_screen(self):
        """
        判断子弹是否超出屏幕
        
        返回:
            bool: 如果子弹离开屏幕返回True，否则返回False
        """
        return self.rect.bottom < 0 or self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        """
        在屏幕上绘制子弹
        
        参数:
            screen: pygame显示表面
        """
        pygame.draw.rect(screen, self.color, self.rect)
        # 绘制子弹高光效果
        pygame.draw.rect(screen, (255, 255, 255), 
                        (self.rect.x + 2, self.rect.y + 2, 
                         self.rect.width - 4, self.rect.height - 4))