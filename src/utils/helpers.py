import os

def get_asset_path(asset_type, filename):
    base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
    return os.path.join(base_path, 'src', 'assets', asset_type, filename)

def load_image(filename):
    import pygame
    path = get_asset_path('images', filename)
    return pygame.image.load(path).convert_alpha()

def load_sound(filename):
    import pygame
    path = get_asset_path('sounds', filename)
    return pygame.mixer.Sound(path)