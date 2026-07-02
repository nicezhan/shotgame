from .constants import LEVELS

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
        enemy_index: 当前生成到的敌人索引
        completed: 关卡是否完成
    """
    
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
            self.enemy_index = 0
            self.completed = False
        else:
            # 所有关卡已完成
            self.config = None
            self.name = "通关！"
            self.enemies = []
            self.spawn_interval = 0
            self.bg_color = (0, 0, 0)
            self.enemy_index = 0
            self.completed = True

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