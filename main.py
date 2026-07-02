import sys
import os

# 将src目录添加到Python路径，使模块可以被导入
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# 导入游戏主类
from game.game import Game

def main():
    """游戏入口函数"""
    # 创建游戏对象并运行
    game = Game()
    game.run()

# 确保脚本直接运行时才执行main函数
if __name__ == '__main__':
    main()