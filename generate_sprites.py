import os
from PIL import Image, ImageDraw

ASSETS_DIR = os.path.join(os.path.dirname(__file__), "src", "assets", "images")
os.makedirs(ASSETS_DIR, exist_ok=True)

def draw_player(base_img, frame_type='idle'):
    draw = ImageDraw.Draw(base_img)
    w, h = base_img.size
    
    cx, cy = w // 2, h // 2
    
    leg_offset = 0
    if frame_type == 'run_1':
        leg_offset = 15
    elif frame_type == 'run_2':
        leg_offset = -15
    
    arm_swing = 0
    if frame_type == 'run_1':
        arm_swing = 20
    elif frame_type == 'run_2':
        arm_swing = -20
    
    # 腿部阴影
    draw.ellipse([cx - 35 - leg_offset, h - 15, cx - 15 - leg_offset, h - 5], fill=(30, 30, 30))
    draw.ellipse([cx + 15 + leg_offset, h - 15, cx + 35 + leg_offset, h - 5], fill=(30, 30, 30))
    
    # 靴子
    draw.rectangle([cx - 40 - leg_offset, h - 35, cx - 15 - leg_offset, h - 15], fill=(40, 40, 40))
    draw.rectangle([cx + 15 + leg_offset, h - 35, cx + 40 + leg_offset, h - 15], fill=(40, 40, 40))
    draw.rectangle([cx - 38 - leg_offset, h - 33, cx - 17 - leg_offset, h - 17], fill=(60, 60, 60))
    draw.rectangle([cx + 17 + leg_offset, h - 33, cx + 38 + leg_offset, h - 17], fill=(60, 60, 60))
    
    # 战术裤
    draw.rectangle([cx - 35 - leg_offset, cy + 30, cx - 18 - leg_offset, h - 35], fill=(100, 100, 120))
    draw.rectangle([cx + 18 + leg_offset, cy + 30, cx + 35 + leg_offset, h - 35], fill=(100, 100, 120))
    
    # 裤线
    draw.line([cx - 26 - leg_offset, cy + 35, cx - 26 - leg_offset, h - 40], fill=(80, 80, 100), width=2)
    draw.line([cx + 26 + leg_offset, cy + 35, cx + 26 + leg_offset, h - 40], fill=(80, 80, 100), width=2)
    
    # 身体（深蓝色作战服）
    draw.ellipse([cx - 35, cy - 20, cx + 35, cy + 45], fill=(40, 60, 120))
    
    # 战术背心
    draw.ellipse([cx - 28, cy - 15, cx + 28, cy + 38], fill=(40, 80, 50))
    draw.ellipse([cx - 24, cy - 10, cx + 24, cy + 33], fill=(30, 60, 40))
    
    # 背心细节
    draw.rectangle([cx - 20, cy - 5, cx + 20, cy + 5], fill=(50, 90, 60))
    draw.rectangle([cx - 15, cy + 10, cx + 15, cy + 25], fill=(50, 90, 60))
    
    # 手臂
    draw.line([cx - 35, cy, cx - 75, cy + 25 + arm_swing], fill=(40, 60, 120), width=15)
    draw.line([cx + 35, cy, cx + 75, cy + 25 - arm_swing], fill=(40, 60, 120), width=15)
    
    # 手套
    draw.ellipse([cx - 85, cy + 18 + arm_swing, cx - 65, cy + 38 + arm_swing], fill=(30, 30, 30))
    draw.ellipse([cx + 65, cy + 18 - arm_swing, cx + 85, cy + 38 - arm_swing], fill=(30, 30, 30))
    
    # 头部（头盔）
    draw.ellipse([cx - 30, cy - 70, cx + 30, cy - 10], fill=(50, 70, 140))
    
    # 头盔高光
    draw.ellipse([cx - 25, cy - 65, cx + 10, cy - 15], fill=(70, 90, 160))
    
    # 头盔面罩
    draw.ellipse([cx - 32, cy - 65, cx + 32, cy - 20], fill=(120, 180, 220), outline=(100, 160, 200), width=3)
    
    # 护目镜
    draw.rectangle([cx - 25, cy - 55, cx + 25, cy - 35], fill=(150, 150, 160))
    draw.rectangle([cx - 22, cy - 52, cx - 2, cy - 38], fill=(20, 20, 30))
    draw.rectangle([cx + 2, cy - 52, cx + 22, cy - 38], fill=(20, 20, 30))
    
    # 护目镜反光
    draw.line([cx - 18, cy - 48, cx - 8, cy - 42], fill=(100, 100, 110), width=2)
    draw.line([cx + 8, cy - 48, cx + 18, cy - 42], fill=(100, 100, 110), width=2)
    
    # 面罩下半部分
    draw.rectangle([cx - 22, cy - 30, cx + 22, cy - 12], fill=(15, 15, 25))
    
    # M4A1步枪
    gun_y = cy + 10
    
    # 枪托
    draw.rectangle([cx + 35, gun_y, cx + 55, gun_y + 25], fill=(80, 50, 30))
    
    # 枪身
    draw.rectangle([cx + 20, gun_y + 5, cx + 75, gun_y + 15], fill=(40, 40, 40))
    
    # 枪管
    draw.rectangle([cx + 75, gun_y + 7, cx + 105, gun_y + 13], fill=(70, 70, 70))
    
    # 弹匣
    draw.rectangle([cx + 35, gun_y + 15, cx + 50, gun_y + 30], fill=(50, 50, 50))
    
    # 握把
    draw.rectangle([cx + 25, gun_y + 15, cx + 35, gun_y + 28], fill=(70, 40, 20))
    
    # 枪口火焰（射击时）
    if frame_type == 'shoot':
        draw.ellipse([cx + 100, gun_y - 10, cx + 120, gun_y + 10], fill=(255, 200, 50))
        draw.ellipse([cx + 105, gun_y - 5, cx + 115, gun_y + 5], fill=(255, 100, 0))
    
    return base_img

def draw_enemy(base_img, enemy_type='minion'):
    draw = ImageDraw.Draw(base_img)
    w, h = base_img.size
    
    cx, cy = w // 2, h // 2
    
    if enemy_type == 'minion':
        pants_color = (139, 69, 19)
        shirt_color = (70, 70, 80)
        vest_color = (90, 90, 90)
        headband_color = (139, 69, 19)
        skin_color = (255, 180, 120)
        glove_color = (150, 40, 40)
        eye_color = (255, 0, 0)
    elif enemy_type == 'elite':
        pants_color = (100, 60, 40)
        shirt_color = (255, 69, 0)
        vest_color = (150, 50, 30)
        headband_color = (255, 0, 0)
        skin_color = (255, 200, 150)
        glove_color = (200, 50, 0)
        eye_color = (255, 200, 0)
    else:
        pants_color = (100, 50, 50)
        shirt_color = (60, 20, 80)
        vest_color = (80, 30, 60)
        headband_color = (150, 0, 150)
        skin_color = (200, 120, 100)
        glove_color = (100, 0, 100)
        eye_color = (200, 0, 255)
    
    # 腿部阴影
    draw.ellipse([cx - 35, h - 15, cx - 15, h - 5], fill=(30, 30, 30))
    draw.ellipse([cx + 15, h - 15, cx + 35, h - 5], fill=(30, 30, 30))
    
    # 靴子
    draw.rectangle([cx - 40, h - 35, cx - 15, h - 15], fill=(40, 40, 40))
    draw.rectangle([cx + 15, h - 35, cx + 40, h - 15], fill=(40, 40, 40))
    
    # 裤子
    draw.rectangle([cx - 35, cy + 30, cx - 18, h - 35], fill=pants_color)
    draw.rectangle([cx + 18, cy + 30, cx + 35, h - 35], fill=pants_color)
    
    # 身体
    draw.ellipse([cx - 35, cy - 20, cx + 35, cy + 45], fill=shirt_color)
    
    # 战术背心
    draw.ellipse([cx - 28, cy - 15, cx + 28, cy + 38], fill=vest_color)
    
    # BOSS护甲
    if enemy_type == 'boss':
        draw.ellipse([cx - 24, cy - 10, cx + 24, cy + 33], fill=(100, 0, 100))
    
    # 手臂
    draw.line([cx - 35, cy, cx - 75, cy + 25], fill=shirt_color, width=15)
    draw.line([cx + 35, cy, cx + 75, cy + 25], fill=shirt_color, width=15)
    
    # 手套
    draw.ellipse([cx - 85, cy + 18, cx - 65, cy + 38], fill=glove_color)
    draw.ellipse([cx + 65, cy + 18, cx + 85, cy + 38], fill=glove_color)
    
    # 头带
    draw.rectangle([cx - 38, cy - 75, cx + 38, cy - 60], fill=headband_color)
    
    # 头部
    draw.ellipse([cx - 30, cy - 60, cx + 30, cy - 5], fill=skin_color)
    
    # 眉毛
    draw.line([cx - 22, cy - 45, cx - 10, cy - 48], fill=(20, 20, 20), width=4)
    draw.line([cx + 10, cy - 48, cx + 22, cy - 45], fill=(20, 20, 20), width=4)
    
    # 眼睛
    if enemy_type == 'minion':
        draw.polygon([(cx - 15, cy - 38), (cx - 20, cy - 45), (cx - 10, cy - 45)], fill=eye_color)
        draw.polygon([(cx + 15, cy - 38), (cx + 20, cy - 45), (cx + 10, cy - 45)], fill=eye_color)
    else:
        draw.ellipse([cx - 18, cy - 42, cx - 8, cy - 32], fill=eye_color)
        draw.ellipse([cx + 8, cy - 42, cx + 18, cy - 32], fill=eye_color)
        draw.ellipse([cx - 15, cy - 40, cx - 11, cy - 34], fill=(255, 255, 255))
        draw.ellipse([cx + 11, cy - 40, cx + 15, cy - 34], fill=(255, 255, 255))
    
    # 鼻子
    draw.polygon([(cx, cy - 30), (cx - 5, cy - 22), (cx + 5, cy - 22)], fill=(200, 150, 100))
    
    # 嘴巴（咬牙）
    draw.line([cx - 12, cy - 18, cx + 12, cy - 18], fill=(20, 20, 20), width=3)
    
    # 胡须
    draw.arc([cx - 25, cy - 20, cx + 25, cy + 15], 0.3, 2.8, fill=(20, 20, 20), width=4)
    
    # AK47步枪
    gun_y = cy + 10
    
    # 枪托
    draw.rectangle([cx - 55, gun_y, cx - 35, gun_y + 25], fill=(80, 50, 30))
    
    # 枪身
    draw.rectangle([cx - 75, gun_y + 5, cx - 20, gun_y + 15], fill=(40, 40, 40))
    
    # 枪管
    draw.rectangle([cx - 105, gun_y + 7, cx - 75, gun_y + 13], fill=(70, 70, 70))
    
    # 弹匣
    draw.rectangle([cx - 55, gun_y + 15, cx - 40, gun_y + 30], fill=(50, 50, 50))
    
    # 握把
    draw.rectangle([cx - 45, gun_y + 15, cx - 35, gun_y + 28], fill=(70, 40, 20))
    
    return base_img

print("Generating player sprites...")

player_idle = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
player_idle = draw_player(player_idle, 'idle')
player_idle.save(os.path.join(ASSETS_DIR, 'player_idle.png'))
print("OK player_idle.png")

player_run_1 = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
player_run_1 = draw_player(player_run_1, 'run_1')
player_run_1.save(os.path.join(ASSETS_DIR, 'player_run_1.png'))
print("OK player_run_1.png")
player_run_2 = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
player_run_2 = draw_player(player_run_2, 'run_2')
player_run_2.save(os.path.join(ASSETS_DIR, 'player_run_2.png'))
print("OK player_run_2.png")
player_shoot = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
player_shoot = draw_player(player_shoot, 'shoot')
player_shoot.save(os.path.join(ASSETS_DIR, 'player_shoot.png'))
print("OK player_shoot.png")

print("\nGenerating enemy sprites...")

enemy_minion = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
enemy_minion = draw_enemy(enemy_minion, 'minion')
enemy_minion.save(os.path.join(ASSETS_DIR, 'enemy_minion.png'))
print("OK enemy_minion.png")

enemy_elite = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
enemy_elite = draw_enemy(enemy_elite, 'elite')
enemy_elite.save(os.path.join(ASSETS_DIR, 'enemy_elite.png'))
print("OK enemy_elite.png")

enemy_boss = Image.new('RGBA', (200, 250), (0, 0, 0, 0))
enemy_boss = draw_enemy(enemy_boss, 'boss')
enemy_boss.save(os.path.join(ASSETS_DIR, 'enemy_boss.png'))
print("OK enemy_boss.png")

print("\nAll sprites generated!")