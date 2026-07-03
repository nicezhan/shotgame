# Shooter Game

一个使用 Python Pygame 开发的射击游戏项目。

## 🎮 游戏特性

- 10个精心设计的关卡，难度逐步递增
- 3种敌人类型：普通小怪、精英小怪、BOSS
- 独特的关卡背景图片，增强游戏氛围
- 流畅的玩家动画效果（跑步、射击）
- 完整的游戏状态管理（菜单、游戏中、暂停、游戏结束）
- 生命值、分数、关卡显示等UI元素

## 📁 项目结构

```
shooter-game/
├── src/
│   ├── game/
│   │   ├── __init__.py
│   │   ├── bullet.py      # 子弹类
│   │   ├── constants.py   # 游戏常量配置
│   │   ├── enemy.py       # 敌人类
│   │   ├── game.py        # 游戏主逻辑
│   │   ├── level.py       # 关卡管理
│   │   ├── player.py      # 玩家类
│   │   └── ui.py          # UI界面
│   └── assets/
│       └── images/        # 游戏图片资源
├── generate_sprites.py    # 精灵图片生成脚本
├── generate_backgrounds.py # 背景图片生成脚本
└── main.py                # 游戏入口
```

## 🚀 快速开始

### 环境要求

- Python 3.8+
- Pygame 2.0+

### 安装依赖

```bash
pip install pygame
pip install pillow
```

### 运行游戏

```bash
python main.py
```

## 🎯 操作说明

| 操作 | 按键 |
|------|------|
| 移动 | WASD / 方向键 |
| 射击 | 空格键 |
| 暂停 | ESC |
| 重新开始 | R（游戏结束时） |

## 📊 游戏难度

- **关卡系统**：共10关，每5关设置BOSS战
- **难度递增**：每关敌人数量+2，同等级敌人伤害增加10%
- **敌人类型**：
  - 普通小怪：基础攻击5，移动较快
  - 精英小怪：基础攻击10，血量更高
  - BOSS：基础攻击15，血量极高

## 🖼️ 关卡背景

| 关卡 | 名称 | 场景 |
|------|------|------|
| 1 | Training Camp | 训练场 |
| 2 | Forest | 森林 |
| 3 | Jungle | 丛林 |
| 4 | Canyon | 峡谷 |
| 5 | Fortress | 要塞（BOSS战） |
| 6 | Wasteland | 荒原 |
| 7 | Desert | 沙漠 |
| 8 | Volcano | 火山 |
| 9 | Ice Cave | 冰洞 |
| 10 | Final Boss | 最终BOSS战 |

## 📝 开发说明

### 生成精灵图片

```bash
python generate_sprites.py
```

### 生成背景图片

```bash
python generate_backgrounds.py
```

## 📄 许可证

MIT License
