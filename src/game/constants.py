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
# 包含三种敌人：basic(普通), fast(快速), tank(坦克)
ENEMY_TYPES = {
    'basic': {
        'width': 45,
        'height': 55,
        'speed': 2,
        'health': 30,
        'color': (139, 69, 19),
        'score': 100,
        'shoot_interval': 3000
    },
    'fast': {
        'width': 40,
        'height': 45,
        'speed': 4,
        'health': 20,
        'color': (255, 69, 0),
        'score': 150,
        'shoot_interval': 2000
    },
    'tank': {
        'width': 60,
        'height': 70,
        'speed': 1,
        'health': 100,
        'color': (80, 80, 80),
        'score': 300,
        'shoot_interval': 4000
    }
}

# 关卡配置列表
LEVELS = [
    {
        'name': 'Level 1 - Training Camp',
        'enemies': [{'type': 'basic', 'count': 5}],
        'spawn_interval': 2000,
        'bg_color': (30, 30, 50)
    },
    {
        'name': 'Level 2 - Jungle',
        'enemies': [{'type': 'basic', 'count': 5}, {'type': 'fast', 'count': 3}],
        'spawn_interval': 1500,
        'bg_color': (20, 50, 30)
    },
    {
        'name': 'Level 3 - Fortress',
        'enemies': [{'type': 'basic', 'count': 4}, {'type': 'fast', 'count': 4}, {'type': 'tank', 'count': 2}],
        'spawn_interval': 1200,
        'bg_color': (40, 40, 40)
    }
]

# 游戏限制配置
MAX_ENEMIES_ON_SCREEN = 8   # 屏幕上最大敌人数量

# UI配置
FONT_SIZE = 24              # 字体大小
HEALTH_BAR_WIDTH = 200      # 生命值条宽度
HEALTH_BAR_HEIGHT = 20      # 生命值条高度