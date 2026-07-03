import pygame
import os
from .constants import LEVELS, SCREEN_WIDTH, SCREEN_HEIGHT

class Level:
    """
    关卡类，负责管理关卡配置和敌人生成顺序
    
    属性:
        level_index: 当前关卡索引
        config: 当前关卡配置
        name: 关卡名称
        enemies: 敌人类型列表（按生成顺序排列）
        spawn_interval: 敌人生成间隔（毫秒）
        bg_color: 关卡背景颜色
        bg_image: 关卡背景图片
        enemy_index: 当前生成到的敌人索引
        completed: 关卡是否完成
    """
    
    bg_images_cache = {}
    
    def __init__(self, level_index=0):
        """
        初始化关卡
        
        参数:
            level_index: 关卡索引，默认为0（第一关）
        """
        self.level_index = level_index
        self.load_level(level_index)
        
    def load_level(self, level_index):
        """
        加载指定关卡配置
        
        参数:
            level_index: 关卡索引
        """
        if level_index < len(LEVELS):
            # 加载有效关卡配置
            self.config = LEVELS[level_index]
            self.name = self.config['name']
            self.enemies = []
            
            # 将敌人配置展开为列表（便于顺序生成）
            for enemy_config in self.config['enemies']:
                for _ in range(enemy_config['count']):
                    self.enemies.append(enemy_config['type'])
            
            self.spawn_interval = self.config['spawn_interval']
            self.bg_color = self.config['bg_color']
            self.bg_image_filename = self.config.get('bg_image')
            self.bg_image = None
            self.enemy_index = 0
            self.completed = False
        else:
            # 所有关卡已完成
            self.config = None
            self.name = "通关！"
            self.enemies = []
            self.spawn_interval = 0
            self.bg_color = (0, 0, 0)
            self.bg_image = None
            self.enemy_index = 0
            self.completed = True
    
    def ensure_bg_image_loaded(self):
        """
        延迟加载背景图片（确保在pygame.display初始化后调用）
        
        返回:
            pygame.Surface or None: 背景图片，加载失败返回None
        """
        if self.bg_image is not None:
            return self.bg_image
        
        if not self.bg_image_filename:
            return None
        
        if self.bg_image_filename in self.bg_images_cache:
            self.bg_image = self.bg_images_cache[self.bg_image_filename]
            return self.bg_image
        
        current_dir = os.path.dirname(os.path.abspath(__file__))
        images_dir = os.path.join(current_dir, "..", "assets", "images")
        images_dir = os.path.normpath(images_dir)
        full_path = os.path.join(images_dir, self.bg_image_filename)
        
        try:
            img = pygame.image.load(full_path).convert()
            scaled_img = pygame.transform.scale(img, (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.bg_images_cache[self.bg_image_filename] = scaled_img
            self.bg_image = scaled_img
            print(f"Loaded background: {full_path}")
            return scaled_img
        except Exception as e:
            print(f"Failed to load background {full_path}: {e}")
            return None

    def get_next_enemy_type(self):
        """
        获取下一个要生成的敌人类型
        
        返回:
            str or None: 敌人类型字符串，如果没有更多敌人返回None
        """
        if self.enemy_index < len(self.enemies):
            enemy_type = self.enemies[self.enemy_index]
            self.enemy_index += 1
            return enemy_type
        return None

    def is_level_complete(self):
        """
        判断关卡是否完成（所有敌人已生成）
        
        返回:
            bool: 如果所有敌人都已生成返回True，否则返回False
        """
        return self.enemy_index >= len(self.enemies)

    def next_level(self):
        """
        切换到下一关
        
        返回:
            bool: 如果还有下一关返回True，否则返回False（通关）
        """
        self.level_index += 1
        self.load_level(self.level_index)
        return not self.completed

    def get_total_enemies(self):
        """
        获取关卡总敌人数量
        
        返回:
            int: 敌人总数
        """
        return len(self.enemies)