import pygame
import random
from .constants import ENEMY_TYPES, SCREEN_WIDTH, SCREEN_HEIGHT
from .bullet import Bullet

class Enemy:
    """
    敌人类，负责敌人的移动、射击、碰撞检测和绘制
    
    属性:
        type: 敌人类型（'minion', 'elite', 'boss'）
        width: 敌人宽度
        height: 敌人高度
        speed: 移动速度
        health: 当前生命值
        max_health: 最大生命值
        attack: 攻击力（子弹伤害）
        defense: 防御力（减少受到的伤害）
        color: 敌人颜色
        score: 击杀敌人获得的分数
        shoot_interval: 射击间隔（毫秒）
        rect: pygame.Rect对象，敌人的矩形区域
        move_direction: 水平移动方向（1向右，-1向左）
        last_shoot_time: 上次射击时间
        bullets: 敌人发射的子弹列表
        move_timer: 移动计时
        change_direction_interval: 改变移动方向的间隔时间
    """
    
    def __init__(self, enemy_type='minion'):
        """
        初始化敌人
        
        参数:
            enemy_type: 敌人类型，默认为'minion'
        """
        # 根据敌人类型获取配置
        config = ENEMY_TYPES.get(enemy_type, ENEMY_TYPES['minion'])
        self.type = enemy_type
        self.width = config['width']
        self.height = config['height']
        self.speed = config['speed']
        self.health = config['health']
        self.max_health = config['health']
        self.attack = config['attack']
        self.defense = config['defense']
        self.color = config['color']
        self.score = config['score']
        self.shoot_interval = config['shoot_interval']
        
        # 设置敌人初始位置在屏幕顶部随机位置
        self.rect = pygame.Rect(random.randint(50, SCREEN_WIDTH - self.width - 50),
                               -self.height,
                               self.width, self.height)
        
        # 随机设置初始移动方向
        self.move_direction = random.choice([-1, 1])
        self.last_shoot_time = 0
        self.bullets = []
        self.move_timer = 0
        self.change_direction_interval = random.randint(1000, 3000)

    def update(self, player):
        """
        更新敌人状态，处理移动和射击逻辑
        
        参数:
            player: 玩家对象，用于射击目标
        """
        # 向下移动
        self.rect.y += self.speed
        
        # 更新移动计时器，随机改变水平移动方向
        self.move_timer += 16
        if self.move_timer > self.change_direction_interval:
            self.move_direction *= -1
            self.move_timer = 0
            self.change_direction_interval = random.randint(1000, 3000)
        
        # 水平移动
        self.rect.x += self.move_direction * self.speed * 0.5
        
        # 碰到屏幕边缘时改变方向
        if self.rect.left <= 0 or self.rect.right >= SCREEN_WIDTH:
            self.move_direction *= -1
        
        # 尝试射击
        self.shoot(player)
        
        # 更新敌人子弹
        for bullet in self.bullets[:]:
            bullet.update()
            if bullet.is_off_screen():
                self.bullets.remove(bullet)

    def shoot(self, player):
        """
        敌人射击（带间隔限制），子弹伤害等于敌人攻击力
        
        参数:
            player: 玩家对象（当前未使用，敌人向正下方射击）
        """
        now = pygame.time.get_ticks()
        if now - self.last_shoot_time > self.shoot_interval:
            # 创建子弹，从敌人底部发射，方向向下，伤害等于敌人攻击力
            bullet = Bullet(self.rect.centerx, self.rect.bottom, direction=1, damage=self.attack)
            self.bullets.append(bullet)
            self.last_shoot_time = now

    def take_damage(self, amount):
        """
        敌人受到伤害（考虑防御力减伤）
        
        参数:
            amount: 基础伤害值
            
        返回:
            bool: 如果生命值<=0返回True（敌人死亡），否则返回False
        """
        # 计算实际伤害：基础伤害 - 防御力，最低伤害为1
        actual_damage = max(1, amount - self.defense)
        self.health -= actual_damage
        return self.health <= 0

    def is_off_screen(self):
        """
        判断敌人是否超出屏幕底部
        
        返回:
            bool: 如果敌人离开屏幕返回True，否则返回False
        """
        return self.rect.top > SCREEN_HEIGHT

    def draw(self, screen):
        """
        在屏幕上绘制敌人和子弹
        
        参数:
            screen: pygame显示表面
        """
        # 绘制敌人主体
        pygame.draw.rect(screen, self.color, self.rect)
        # 绘制敌人内部高光
        pygame.draw.rect(screen, (200, 200, 200), 
                        (self.rect.x + 3, self.rect.y + 3, 
                         self.rect.width - 6, self.rect.height - 6))
        
        # 绘制生命值条
        health_ratio = self.health / self.max_health
        health_bar_width = self.rect.width * health_ratio
        pygame.draw.rect(screen, (255, 0, 0), 
                        (self.rect.x, self.rect.y - 5, 
                         self.rect.width, 3))
        pygame.draw.rect(screen, (0, 255, 0), 
                        (self.rect.x, self.rect.y - 5, 
                         health_bar_width, 3))
        
        # 绘制所有子弹
        for bullet in self.bullets:
            bullet.draw(screen)