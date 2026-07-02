import pygame
import os
from .constants import FONT_SIZE, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT, WHITE, RED, GREEN, BLACK, SCREEN_WIDTH, SCREEN_HEIGHT

class UI:
    """
    UI类，负责游戏界面的绘制（生命值、分数、菜单、游戏结束等）
    
    属性:
        font: pygame.font.Font对象，用于绘制文本
    """
    
    def __init__(self):
        """初始化UI，加载字体"""
        pygame.font.init()
        self.font = self._load_chinese_font()
        
    def _load_chinese_font(self):
        """
        尝试加载支持中文的系统字体
        
        返回:
            pygame.font.Font: 可用的字体对象
        """
        # Windows系统常见字体列表
        font_paths = [
            'simhei.ttf',
            'simkai.ttf', 
            'simsun.ttc',
            'msyh.ttc',
            'msyhbd.ttc',
            'msyhl.ttc',
            'simfang.ttf',
            'simli.ttf',
            'STKAITI.TTF',
            'STSONG.TTF',
            'STZHONGS.TTF',
            'STXIHEI.TTF',
            'STXINGKA.TTF',
            'STXINWEI.TTF',
        ]
        
        # 尝试加载每种字体
        for font_name in font_paths:
            try:
                font = pygame.font.SysFont(font_name, FONT_SIZE)
                test_text = font.render("测试", True, WHITE)
                if test_text:
                    return font
            except:
                continue
        
        # 如果没有找到合适的字体，使用默认字体
        try:
            font = pygame.font.SysFont(None, FONT_SIZE)
            return font
        except:
            return pygame.font.Font(None, FONT_SIZE)
        
    def draw_health_bar(self, screen, health, max_health, x, y):
        """
        绘制生命值条
        
        参数:
            screen: pygame显示表面
            health: 当前生命值
            max_health: 最大生命值
            x: 生命值条左上角x坐标
            y: 生命值条左上角y坐标
        """
        health_ratio = health / max_health
        bar_width = HEALTH_BAR_WIDTH * health_ratio
        
        # 绘制背景
        pygame.draw.rect(screen, BLACK, (x, y, HEALTH_BAR_WIDTH, HEALTH_BAR_HEIGHT))
        # 绘制红色背景（损失的生命值）
        pygame.draw.rect(screen, RED, (x + 2, y + 2, HEALTH_BAR_WIDTH - 4, HEALTH_BAR_HEIGHT - 4))
        # 绘制绿色前景（剩余生命值）
        pygame.draw.rect(screen, GREEN, (x + 2, y + 2, bar_width - 4, HEALTH_BAR_HEIGHT - 4))
        
        # 绘制生命值文字
        text = self.font.render(f"{health}/{max_health}", True, WHITE)
        text_rect = text.get_rect(center=(x + HEALTH_BAR_WIDTH // 2, y + HEALTH_BAR_HEIGHT // 2))
        screen.blit(text, text_rect)

    def draw_score(self, screen, score, x, y):
        """
        绘制分数
        
        参数:
            screen: pygame显示表面
            score: 当前分数
            x: 分数左上角x坐标
            y: 分数左上角y坐标
        """
        text = self.font.render(f"Score: {score}", True, WHITE)
        screen.blit(text, (x, y))

    def draw_level(self, screen, level_name, x, y):
        """
        绘制关卡名称
        
        参数:
            screen: pygame显示表面
            level_name: 关卡名称
            x: 关卡名称左上角x坐标
            y: 关卡名称左上角y坐标
        """
        text = self.font.render(f"Level: {level_name}", True, WHITE)
        screen.blit(text, (x, y))

    def draw_enemies_count(self, screen, current, total, x, y):
        """
        绘制敌人击杀计数
        
        参数:
            screen: pygame显示表面
            current: 已击杀敌人数量
            total: 关卡总敌人数量
            x: 计数左上角x坐标
            y: 计数左上角y坐标
        """
        text = self.font.render(f"Enemies: {current}/{total}", True, WHITE)
        screen.blit(text, (x, y))

    def draw_game_over(self, screen, score):
        """
        绘制游戏结束界面
        
        参数:
            screen: pygame显示表面
            score: 最终得分
        """
        # 绘制半透明遮罩
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # 绘制游戏结束文字
        game_over_text = self.font.render("Game Over", True, RED)
        game_over_rect = game_over_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(game_over_text, game_over_rect)
        
        # 绘制最终得分
        score_text = self.font.render(f"Final Score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(score_text, score_rect)
        
        # 绘制重新开始提示
        restart_text = self.font.render("Press R to Restart", True, GREEN)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)

    def draw_menu(self, screen):
        """
        绘制游戏主菜单
        
        参数:
            screen: pygame显示表面
        """
        # 绘制半透明遮罩
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(200)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # 绘制游戏标题
        title_text = self.font.render("Shooter Game", True, WHITE)
        title_rect = title_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 80))
        screen.blit(title_text, title_rect)
        
        # 绘制开始提示
        start_text = self.font.render("Press SPACE to Start", True, GREEN)
        start_rect = start_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(start_text, start_rect)
        
        # 绘制操作说明
        controls_text = self.font.render("WASD/Arrow Keys to Move | SPACE to Shoot", True, WHITE)
        controls_rect = controls_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 80))
        screen.blit(controls_text, controls_rect)

    def draw_level_complete(self, screen, score):
        """
        绘制关卡完成界面
        
        参数:
            screen: pygame显示表面
            score: 当前得分
        """
        # 绘制半透明遮罩
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # 绘制关卡完成文字
        complete_text = self.font.render("Level Complete!", True, GREEN)
        complete_rect = complete_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(complete_text, complete_rect)
        
        # 绘制当前得分
        score_text = self.font.render(f"Current Score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(score_text, score_rect)
        
        # 绘制继续提示
        continue_text = self.font.render("Press SPACE to Continue", True, GREEN)
        continue_rect = continue_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(continue_text, continue_rect)

    def draw_victory(self, screen, score):
        """
        绘制通关界面
        
        参数:
            screen: pygame显示表面
            score: 最终得分
        """
        # 绘制半透明遮罩
        overlay = pygame.Surface((SCREEN_WIDTH, SCREEN_HEIGHT))
        overlay.set_alpha(180)
        overlay.fill(BLACK)
        screen.blit(overlay, (0, 0))
        
        # 绘制通关文字
        victory_text = self.font.render("Victory!", True, GREEN)
        victory_rect = victory_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 - 50))
        screen.blit(victory_text, victory_rect)
        
        # 绘制最终得分
        score_text = self.font.render(f"Final Score: {score}", True, WHITE)
        score_rect = score_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2))
        screen.blit(score_text, score_rect)
        
        # 绘制重新开始提示
        restart_text = self.font.render("Press R to Restart", True, GREEN)
        restart_rect = restart_text.get_rect(center=(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2 + 50))
        screen.blit(restart_text, restart_rect)