from PIL import Image, ImageDraw
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

backgrounds = [
    {'name': 'bg_training_camp', 'theme': 'training', 'colors': [(30, 30, 50), (50, 50, 80), (20, 20, 40)]},
    {'name': 'bg_forest', 'theme': 'forest', 'colors': [(25, 40, 35), (40, 70, 50), (15, 30, 25)]},
    {'name': 'bg_jungle', 'theme': 'jungle', 'colors': [(20, 50, 30), (30, 80, 40), (10, 35, 20)]},
    {'name': 'bg_canyon', 'theme': 'canyon', 'colors': [(60, 40, 20), (90, 60, 30), (40, 25, 10)]},
    {'name': 'bg_fortress', 'theme': 'fortress', 'colors': [(40, 40, 40), (60, 60, 60), (25, 25, 25)]},
    {'name': 'bg_wasteland', 'theme': 'wasteland', 'colors': [(50, 45, 40), (70, 65, 55), (35, 30, 25)]},
    {'name': 'bg_desert', 'theme': 'desert', 'colors': [(60, 50, 30), (90, 75, 45), (40, 30, 15)]},
    {'name': 'bg_volcano', 'theme': 'volcano', 'colors': [(50, 25, 20), (80, 35, 25), (30, 15, 10)]},
    {'name': 'bg_ice_cave', 'theme': 'ice', 'colors': [(40, 50, 60), (60, 80, 100), (25, 35, 45)]},
    {'name': 'bg_final_boss', 'theme': 'boss', 'colors': [(20, 20, 30), (40, 40, 60), (10, 10, 20)]},
]

def generate_gradient_background(base_color, secondary_color, dark_color, width, height):
    img = Image.new('RGB', (width, height), dark_color)
    draw = ImageDraw.Draw(img)
    
    for y in range(height):
        ratio = y / height
        r = int(base_color[0] + (secondary_color[0] - base_color[0]) * (1 - ratio) * 0.5)
        g = int(base_color[1] + (secondary_color[1] - base_color[1]) * (1 - ratio) * 0.5)
        b = int(base_color[2] + (secondary_color[2] - base_color[2]) * (1 - ratio) * 0.5)
        draw.line([(0, y), (width, y)], fill=(r, g, b))
    
    return img

def add_scenery(img, theme):
    draw = ImageDraw.Draw(img)
    width, height = img.size
    
    if theme == 'training':
        draw.rectangle([(50, 400), (150, 450)], fill=(60, 60, 60))
        draw.rectangle([(600, 380), (750, 440)], fill=(60, 60, 60))
        draw.rectangle([(350, 420), (450, 460)], fill=(70, 70, 70))
        for i in range(3):
            draw.line([(80 + i * 30, 400), (80 + i * 30, 380)], fill=(100, 100, 100), width=2)
    
    elif theme == 'forest':
        for i in range(8):
            x = 50 + i * 100
            draw.polygon([(x, height), (x + 30, height - 150), (x + 60, height)], fill=(20, 60, 30))
            draw.polygon([(x + 15, height), (x + 30, height - 100), (x + 45, height)], fill=(30, 80, 40))
    
    elif theme == 'jungle':
        for i in range(6):
            x = 30 + i * 130
            draw.polygon([(x, height), (x + 40, height - 180), (x + 80, height)], fill=(15, 70, 25))
            draw.polygon([(x + 20, height), (x + 40, height - 120), (x + 60, height)], fill=(25, 90, 35))
            draw.polygon([(x + 30, height), (x + 40, height - 70), (x + 50, height)], fill=(35, 110, 45))
    
    elif theme == 'canyon':
        draw.polygon([(0, height), (0, height - 200), (150, height - 100), (250, height)], fill=(50, 30, 15))
        draw.polygon([(width, height), (width, height - 250), (width - 200, height - 80), (width - 300, height)], fill=(60, 35, 18))
        draw.polygon([(300, height), (350, height - 120), (450, height)], fill=(40, 25, 12))
    
    elif theme == 'fortress':
        draw.rectangle([(0, height - 150), (width, height)], fill=(50, 50, 50))
        draw.rectangle([(200, height - 200), (250, height - 150)], fill=(70, 70, 70))
        draw.rectangle([(550, height - 220), (600, height - 150)], fill=(70, 70, 70))
        draw.rectangle([(350, height - 250), (450, height - 150)], fill=(80, 80, 80))
        draw.rectangle([(380, height - 280), (420, height - 250)], fill=(90, 90, 90))
    
    elif theme == 'wasteland':
        draw.rectangle([(0, height - 100), (width, height)], fill=(45, 40, 35))
        for i in range(5):
            x = 100 + i * 140
            draw.polygon([(x, height), (x + 5, height - 40), (x + 10, height)], fill=(35, 30, 25))
    
    elif theme == 'desert':
        draw.rectangle([(0, height - 80), (width, height)], fill=(70, 55, 30))
        for i in range(6):
            x = 80 + i * 120
            y = height - 80
            draw.polygon([(x, y), (x + 25, y - 50), (x + 50, y)], fill=(60, 45, 25))
    
    elif theme == 'volcano':
        draw.rectangle([(0, height - 120), (width, height)], fill=(60, 25, 20))
        draw.polygon([(width // 2, height - 300), (width // 2 - 100, height - 120), (width // 2 + 100, height - 120)], fill=(80, 30, 25))
        draw.polygon([(width // 2, height - 350), (width // 2 - 40, height - 300), (width // 2 + 40, height - 300)], fill=(100, 40, 30))
        for i in range(3):
            draw.ellipse([(width // 2 - 10 + i * 5, height - 360 - i * 20), 
                          (width // 2 + 10 + i * 5, height - 340 - i * 20)], fill=(255, 100, 50))
    
    elif theme == 'ice':
        draw.rectangle([(0, height - 100), (width, height)], fill=(60, 90, 120))
        for i in range(4):
            x = 150 + i * 150
            draw.polygon([(x, height), (x + 30, height - 80), (x + 60, height)], fill=(80, 120, 160))
            draw.polygon([(x + 15, height), (x + 30, height - 50), (x + 45, height)], fill=(100, 140, 180))
    
    elif theme == 'boss':
        draw.rectangle([(0, height - 80), (width, height)], fill=(30, 30, 50))
        draw.rectangle([(100, height - 200), (700, height - 80)], fill=(40, 40, 60))
        draw.rectangle([(300, height - 280), (500, height - 200)], fill=(50, 50, 80))
        for i in range(5):
            draw.ellipse([(200 + i * 100, height - 150), (220 + i * 100, height - 130)], fill=(100, 100, 150))
    
    return img

output_dir = os.path.join(os.path.dirname(__file__), 'assets', 'images', 'backgrounds')
os.makedirs(output_dir, exist_ok=True)

for bg in backgrounds:
    img = generate_gradient_background(bg['colors'][0], bg['colors'][1], bg['colors'][2], SCREEN_WIDTH, SCREEN_HEIGHT)
    img = add_scenery(img, bg['theme'])
    filepath = os.path.join(output_dir, f"{bg['name']}.png")
    img.save(filepath, 'PNG')
    print(f"Generated: {bg['name']}.png - Size: {img.size}")

print("OK")
