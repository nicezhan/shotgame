# 游戏屏幕配置
SCREEN_WIDTH = 800       # 屏幕宽度
SCREEN_HEIGHT = 600      # 屏幕高度
FPS = 60                 # 帧率

# 颜色定义 (RGB格式)
WHITE = (255, 255, 255)     # 白色
BLACK = (0, 0, 0)           # 黑色
RED = (255, 0, 0)           # 红色
GREEN = (0, 255, 0)         # 绿色
BLUE = (0, 0, 255)          # 蓝色
GRAY = (128, 128, 128)      # 灰色
DARK_GRAY = (50, 50, 50)    # 深灰色

# 玩家配置
PLAYER_WIDTH = 50           # 玩家宽度
PLAYER_HEIGHT = 60          # 玩家高度
PLAYER_SPEED = 5            # 玩家移动速度
PLAYER_HEALTH = 100         # 玩家初始生命值
PLAYER_COLOR = (70, 130, 180)  # 玩家颜色（蓝色）

# 子弹配置
BULLET_WIDTH = 8            # 子弹宽度
BULLET_HEIGHT = 15          # 子弹高度
BULLET_SPEED = 10           # 子弹速度
BULLET_COLOR = (255, 200, 0)   # 敌人子弹颜色（黄色）
PLAYER_BULLET_COLOR = (0, 255, 255)  # 玩家子弹颜色（青色）

# 敌人基础配置
ENEMY_WIDTH = 45            # 敌人宽度
ENEMY_HEIGHT = 55           # 敌人高度
ENEMY_SPEED = 2             # 敌人移动速度
ENEMY_HEALTH = 30           # 敌人基础生命值
ENEMY_COLOR = (139, 69, 19) # 敌人基础颜色（棕色）
ENEMY_SPAWN_INTERVAL = 2000 # 敌人生成间隔（毫秒）

# 敌人类型配置字典
# 包含三种敌人：minion(普通小怪), elite(精英小怪), boss(BOSS)
# 属性说明:
#   width/height: 敌人尺寸
#   speed: 移动速度
#   health: 生命值
#   attack: 攻击力（子弹伤害）
#   defense: 防御力（减少受到的伤害）
#   color: 敌人颜色
#   score: 击杀获得分数
#   shoot_interval: 射击间隔（毫秒）
ENEMY_TYPES = {
    'minion': {
        'width': 45,
        'height': 55,
        'speed': 1.33,
        'health': 30,
        'attack': 5,
        'defense': 0,
        'color': (139, 69, 19),
        'score': 100,
        'shoot_interval': 3000
    },
    'elite': {
        'width': 50,
        'height': 60,
        'speed': 2,
        'health': 60,
        'attack': 10,
        'defense': 5,
        'color': (255, 69, 0),
        'score': 250,
        'shoot_interval': 2000
    },
    'boss': {
        'width': 100,
        'height': 120,
        'speed': 0.67,
        'health': 500,
        'attack': 15,
        'defense': 15,
        'color': (128, 0, 128),
        'score': 1000,
        'shoot_interval': 1500
    }
}

# 难度递增配置
DIFFICULTY_PER_LEVEL = 0.10

# 关卡配置列表
LEVELS = [
    {
        'name': 'Level 1 - Training Camp',
        'enemies': [{'type': 'minion', 'count': 5}],
        'spawn_interval': 2000,
        'bg_color': (30, 30, 50),
        'bg_image': 'bg_training_camp.png'
    },
    {
        'name': 'Level 2 - Forest',
        'enemies': [{'type': 'minion', 'count': 7}],
        'spawn_interval': 1900,
        'bg_color': (25, 40, 35),
        'bg_image': 'bg_forest.png'
    },
    {
        'name': 'Level 3 - Jungle',
        'enemies': [{'type': 'minion', 'count': 7}, {'type': 'elite', 'count': 2}],
        'spawn_interval': 1800,
        'bg_color': (20, 50, 30),
        'bg_image': 'bg_jungle.png'
    },
    {
        'name': 'Level 4 - Canyon',
        'enemies': [{'type': 'minion', 'count': 7}, {'type': 'elite', 'count': 4}],
        'spawn_interval': 1700,
        'bg_color': (60, 40, 20),
        'bg_image': 'bg_canyon.png'
    },
    {
        'name': 'Level 5 - Fortress',
        'enemies': [{'type': 'minion', 'count': 6}, {'type': 'elite', 'count': 4}, {'type': 'boss', 'count': 1}],
        'spawn_interval': 1600,
        'bg_color': (40, 40, 40),
        'bg_image': 'bg_fortress.png'
    },
    {
        'name': 'Level 6 - Wasteland',
        'enemies': [{'type': 'minion', 'count': 9}, {'type': 'elite', 'count': 4}],
        'spawn_interval': 1500,
        'bg_color': (50, 45, 40),
        'bg_image': 'bg_wasteland.png'
    },
    {
        'name': 'Level 7 - Desert',
        'enemies': [{'type': 'minion', 'count': 9}, {'type': 'elite', 'count': 6}],
        'spawn_interval': 1450,
        'bg_color': (60, 50, 30),
        'bg_image': 'bg_desert.png'
    },
    {
        'name': 'Level 8 - Volcano',
        'enemies': [{'type': 'minion', 'count': 10}, {'type': 'elite', 'count': 8}],
        'spawn_interval': 1400,
        'bg_color': (50, 25, 20),
        'bg_image': 'bg_volcano.png'
    },
    {
        'name': 'Level 9 - Ice Cave',
        'enemies': [{'type': 'minion', 'count': 10}, {'type': 'elite', 'count': 10}],
        'spawn_interval': 1350,
        'bg_color': (40, 50, 60),
        'bg_image': 'bg_ice_cave.png'
    },
    {
        'name': 'Level 10 - Final Boss',
        'enemies': [{'type': 'minion', 'count': 8}, {'type': 'elite', 'count': 8}, {'type': 'boss', 'count': 1}],
        'spawn_interval': 1300,
        'bg_color': (20, 20, 30),
        'bg_image': 'bg_final_boss.png'
    }
]

# 游戏限制配置
MAX_ENEMIES_ON_SCREEN = 8   # 屏幕上最大敌人数量

# UI配置
FONT_SIZE = 24              # 字体大小
HEALTH_BAR_WIDTH = 200      # 生命值条宽度
HEALTH_BAR_HEIGHT = 20      # 生命值条高度