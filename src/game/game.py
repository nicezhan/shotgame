import pygame
import sys
from .constants import SCREEN_WIDTH, SCREEN_HEIGHT, FPS, MAX_ENEMIES_ON_SCREEN
from .states import GameState
from .player import Player
from .enemy import Enemy
from .level import Level
from .ui import UI

class Game:
    """
    游戏主类，负责游戏循环、状态管理和整体协调
    
    属性:
        screen: pygame显示表面
        clock: pygame时钟对象，用于控制帧率
        current_state: 当前游戏状态（MENU/PLAYING/PAUSED/GAME_OVER）
        running: 游戏是否运行中
        ui: UI对象，负责界面绘制
        player: 玩家对象
        enemies: 当前屏幕上的敌人列表
        level: 当前关卡对象
        score: 当前分数
        last_spawn_time: 上次敌人生成时间
        enemies_killed: 已击杀敌人数量
    """
    
    def __init__(self):
        """初始化游戏，设置窗口和基本属性"""
        pygame.init()
        
        # 创建游戏窗口
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Shooter Game')
        
        # 初始化游戏时钟
        self.clock = pygame.time.Clock()
        
        # 设置初始游戏状态
        self.current_state = GameState.MENU
        self.running = True
        
        # 创建UI和重置游戏
        self.ui = UI()
        self.reset_game()

    def reset_game(self):
        """重置游戏状态，开始新游戏"""
        self.player = Player()
        self.enemies = []
        self.level = Level()
        self.score = 0
        self.last_spawn_time = 0
        self.enemies_killed = 0

    def handle_events(self):
        """处理游戏事件（键盘输入、窗口关闭等）"""
        for event in pygame.event.get():
            # 关闭窗口事件
            if event.type == pygame.QUIT:
                self.running = False
            
            # 键盘按下事件
            if event.type == pygame.KEYDOWN:
                # 菜单状态：按空格键开始游戏
                if self.current_state == GameState.MENU:
                    if event.key == pygame.K_SPACE:
                        self.current_state = GameState.PLAYING
                
                # 游戏结束状态：按R键重新开始
                elif self.current_state == GameState.GAME_OVER:
                    if event.key == pygame.K_r:
                        self.reset_game()
                        self.current_state = GameState.MENU
                
                # 游戏中状态：按空格键射击
                elif self.current_state == GameState.PLAYING:
                    if event.key == pygame.K_SPACE:
                        self.player.shoot()
                
                # 暂停状态：按空格键继续
                elif self.current_state == GameState.PAUSED:
                    if event.key == pygame.K_SPACE:
                        self.current_state = GameState.PLAYING
                
                # 按P键切换暂停/继续
                elif event.key == pygame.K_p:
                    if self.current_state == GameState.PLAYING:
                        self.current_state = GameState.PAUSED
                    elif self.current_state == GameState.PAUSED:
                        self.current_state = GameState.PLAYING

    def spawn_enemy(self):
        """根据关卡配置生成敌人（带间隔限制和数量限制）"""
        now = pygame.time.get_ticks()
        
        # 检查是否达到生成间隔
        if now - self.last_spawn_time > self.level.spawn_interval:
            # 检查屏幕上敌人数量是否达到上限
            if len(self.enemies) < MAX_ENEMIES_ON_SCREEN:
                # 获取下一个要生成的敌人类型
                enemy_type = self.level.get_next_enemy_type()
                if enemy_type:
                    # 创建敌人并添加到列表
                    enemy = Enemy(enemy_type)
                    self.enemies.append(enemy)
                    self.last_spawn_time = now

    def update(self):
        """更新游戏状态（玩家、敌人、碰撞检测等）"""
        if self.current_state == GameState.PLAYING:
            # 获取当前按键状态并处理玩家移动
            keys = pygame.key.get_pressed()
            self.player.handle_input(keys)
            
            # 尝试生成敌人
            self.spawn_enemy()
            
            # 更新玩家状态（子弹、碰撞检测）
            self.player.update(self.enemies)
            
            # 更新所有敌人状态
            for enemy in self.enemies[:]:
                enemy.update(self.player)
                
                # 移除超出屏幕的敌人
                if enemy.is_off_screen():
                    self.enemies.remove(enemy)
                    continue
                
                # 检测敌人子弹与玩家的碰撞
                for bullet in enemy.bullets[:]:
                    if bullet.rect.colliderect(self.player.rect):
                        enemy.bullets.remove(bullet)
                        # 玩家受到伤害，如果死亡则游戏结束
                        if self.player.take_damage(10):
                            self.current_state = GameState.GAME_OVER
                        break
                
                # 检查敌人是否被击杀
                if enemy.health <= 0:
                    self.score += enemy.score
                    self.enemies_killed += 1
                    self.enemies.remove(enemy)
            
            # 检查关卡是否完成
            if self.level.is_level_complete() and len(self.enemies) == 0:
                # 切换到下一关，如果没有下一关则通关
                if self.level.next_level():
                    self.current_state = GameState.PAUSED
                else:
                    self.current_state = GameState.GAME_OVER

    def render(self):
        """绘制游戏界面"""
        # 填充背景色
        self.screen.fill(self.level.bg_color)
        
        # 游戏中或暂停状态：绘制玩家、敌人和UI
        if self.current_state == GameState.PLAYING or self.current_state == GameState.PAUSED:
            self.player.draw(self.screen)
            
            for enemy in self.enemies:
                enemy.draw(self.screen)
            
            # 绘制UI元素
            self.ui.draw_health_bar(self.screen, self.player.health, self.player.max_health, 10, 10)
            self.ui.draw_score(self.screen, self.score, SCREEN_WIDTH - 120, 10)
            self.ui.draw_level(self.screen, self.level.name, 10, 40)
            self.ui.draw_enemies_count(self.screen, self.enemies_killed, self.level.get_total_enemies(), SCREEN_WIDTH - 150, 40)
        
        # 菜单状态：绘制主菜单
        if self.current_state == GameState.MENU:
            self.ui.draw_menu(self.screen)
        
        # 游戏结束状态：绘制游戏结束或通关界面
        elif self.current_state == GameState.GAME_OVER:
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)
            if self.level.completed:
                self.ui.draw_victory(self.screen, self.score)
            else:
                self.ui.draw_game_over(self.screen, self.score)
        
        # 暂停状态（关卡完成）：绘制关卡完成界面
        elif self.current_state == GameState.PAUSED:
            self.player.draw(self.screen)
            for enemy in self.enemies:
                enemy.draw(self.screen)
            self.ui.draw_level_complete(self.screen, self.score)
        
        # 更新显示
        pygame.display.flip()

    def run(self):
        """游戏主循环"""
        while self.running:
            # 处理事件
            self.handle_events()
            
            # 更新状态
            self.update()
            
            # 绘制界面
            self.render()
            
            # 控制帧率
            self.clock.tick(FPS)
        
        # 退出游戏
        pygame.quit()
        sys.exit()